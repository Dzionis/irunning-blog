#!/usr/bin/env python3
"""Builds the "Central Park Loop" GPX used for the run-video figures.

Why this exists: the app's --seed-share-run route is a synthetic loop that cuts
through buildings, which looks wrong on a satellite map. This script makes a run
that follows the real park drives (West Drive → East Drive → Center Drive) and
adds timestamps + heart rate so the app imports it as a normal run.

Steps:
  1. Fetch the drive ways from Overpass (falls back to the cached
     central-park-loop-drives.json when the API is busy).
  2. Route between waypoints on a graph made only of those drives
     (Dijkstra), so nothing leaves the park.
  3. Sample every 5 s at a pace plan (easy → 5 × 1 km surges with floats →
     easy) with a drifting heart rate, ~1 m GPS jitter.
  4. Write central-park-loop.gpx (Garmin TrackPointExtension hr).

Import it on the simulator by copying it into the Files app's local storage:
  ~/Library/Developer/CoreSimulator/Devices/<udid>/data/Containers/Shared/AppGroup/<group.com.apple.FileProvider.LocalStorage>/File Provider Storage/
then iRunning › History › import icon › "GPX or FIT file" › Browse › On My iPhone.

Usage: python3 make-central-park-loop.py [--refetch]
"""
import bisect, heapq, json, math, os, random, sys, urllib.parse, urllib.request
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'central-park-loop-drives.json')
OUT = os.path.join(HERE, 'central-park-loop.gpx')


def dist(a, b):
    la1, lo1 = a; la2, lo2 = b
    x = (lo2 - lo1) * math.cos(math.radians((la1 + la2) / 2)) * 111320
    y = (la2 - la1) * 110574
    return math.hypot(x, y)


def fetch_drives():
    q = ('[out:json][timeout:60];('
         'way["highway"]["name"~"Drive|Crossing|Loop"](40.764,-73.984,40.801,-73.948);'
         'way["highway"](40.7640,-73.9800,40.7700,-73.9715););out geom;')
    for host in ('lz4.overpass-api.de', 'overpass-api.de', 'z.overpass-api.de'):
        try:
            req = urllib.request.Request(f'https://{host}/api/interpreter',
                                         data=urllib.parse.urlencode({'data': q}).encode(),
                                         headers={'User-Agent': 'irunning-blog-figures/1.0'})
            data = urllib.request.urlopen(req, timeout=120).read()
            return json.loads(data)['elements']
        except Exception as e:  # busy mirror, try the next one
            print('overpass', host, 'failed:', e, file=sys.stderr)
    raise SystemExit('no Overpass mirror answered')


def build_route(elements):
    keep = {'West Drive', 'East Drive', 'Center Drive'}
    types = ('service', 'unclassified', 'pedestrian', 'living_street', 'cycleway', 'residential')
    adj, owner = {}, {}
    key = lambda g: (round(g['lat'], 7), round(g['lon'], 7))
    for w in elements:
        t = w.get('tags', {})
        if 'geometry' not in w or t.get('highway') not in types:
            continue
        name = t.get('name')
        # Named drives anywhere in the park, plus every small road in the
        # south-east corner (the unnamed connector between East and Center Drive).
        se_corner = all(40.7640 <= g['lat'] <= 40.7700 and -73.9800 <= g['lon'] <= -73.9715 for g in w['geometry'])
        if name not in keep and not se_corner:
            continue
        g = [key(x) for x in w['geometry']]
        for n in g:
            owner.setdefault(n, name or '?')
        for a, b in zip(g, g[1:]):
            adj.setdefault(a, {})[b] = dist(a, b)
            adj.setdefault(b, {})[a] = dist(a, b)
    nodes = list(adj)

    def nearest(p, name):
        return min((n for n in nodes if owner[n] == name), key=lambda n: dist(n, p))

    def dijkstra(s, t):
        dd, prev, pq = {s: 0}, {}, [(0, s)]
        while pq:
            c, u = heapq.heappop(pq)
            if u == t:
                break
            if c > dd.get(u, 1e18):
                continue
            for v, w in adj[u].items():
                if c + w < dd.get(v, 1e18):
                    dd[v] = c + w; prev[v] = u; heapq.heappush(pq, (c + w, v))
        path = [t]
        while path[-1] != s:
            path.append(prev[path[-1]])
        return path[::-1]

    W, E, C = 'West Drive', 'East Drive', 'Center Drive'
    wps = [((40.7688, -73.9812), W), ((40.7740, -73.9759), W), ((40.7830, -73.9690), W), ((40.7920, -73.9620), W),
           ((40.7985, -73.9570), W), ((40.7985, -73.9540), E), ((40.7920, -73.9560), E), ((40.7840, -73.9591), E),
           ((40.7740, -73.9692), E), ((40.7660, -73.9735), E), ((40.7670, -73.9769), C), ((40.7688, -73.9812), W)]
    route = []
    for (a, na), (b, nb) in zip(wps, wps[1:]):
        p = dijkstra(nearest(a, na), nearest(b, nb))
        route += p if not route else p[1:]
    return route


def write_gpx(route):
    cum = [0.0]
    for a, b in zip(route, route[1:]):
        cum.append(cum[-1] + dist(a, b))
    L = cum[-1]
    # (start m, end m, sec/km, hr from, hr to)
    plan = [(0, 1500, 350, 124, 150)]
    x = 1500
    for _ in range(5):
        plan.append((x, x + 1000, 275, 158, 178)); x += 1000
        plan.append((x, x + 500, 345, 168, 150)); x += 500
    plan.append((x, L, 355, 150, 128))

    def pace_hr(m):
        for s, e, p, h0, h1 in plan:
            if s <= m < e or (e >= L and m >= s):
                return p, h0 + (h1 - h0) * min(1, (m - s) / max(1, e - s))
        return 355, 130

    random.seed(7)
    t0 = datetime(2026, 9, 15, 5, 3, 0, tzinfo=timezone.utc)
    pts, m, t, hr = [], 0.0, 0.0, 130.0
    while m < L:
        p, hr_t = pace_hr(m)
        hr += (hr_t - hr) * 0.12 + random.uniform(-1.2, 1.2)
        i = min(bisect.bisect_right(cum, m) - 1, len(route) - 2)
        f = (m - cum[i]) / max(1e-6, cum[i + 1] - cum[i]); a, b = route[i], route[i + 1]
        la = a[0] + (b[0] - a[0]) * f + random.gauss(0, 0.7e-5)
        lo = a[1] + (b[1] - a[1]) * f + random.gauss(0, 0.9e-5)
        pts.append((t, la, lo, int(round(hr))))
        m += 5.0 / (p / 1000.0); t += 5.0
    iso = lambda s: (t0 + timedelta(seconds=s)).strftime('%Y-%m-%dT%H:%M:%SZ')
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<gpx version="1.1" creator="iRunning blog" xmlns="http://www.topografix.com/GPX/1/1" '
             'xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">',
             f' <metadata><time>{iso(0)}</time></metadata>',
             ' <trk><name>Central Park Loop</name><type>running</type><trkseg>']
    for t, la, lo, h in pts:
        lines.append(f'  <trkpt lat="{la:.7f}" lon="{lo:.7f}"><time>{iso(t)}</time><extensions>'
                     f'<gpxtpx:TrackPointExtension><gpxtpx:hr>{h}</gpxtpx:hr></gpxtpx:TrackPointExtension></extensions></trkpt>')
    lines.append(' </trkseg></trk></gpx>')
    open(OUT, 'w').write('\n'.join(lines))
    print(f'{OUT}: {L:.0f} m, {int(t // 60)}:{int(t % 60):02d}, {len(pts)} points')


if __name__ == '__main__':
    if '--refetch' in sys.argv or not os.path.exists(CACHE):
        route = build_route(fetch_drives())
        json.dump(route, open(CACHE, 'w'))
    else:
        route = [tuple(p) for p in json.load(open(CACHE))]
    write_gpx(route)
