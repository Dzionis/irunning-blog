#!/usr/bin/env python3
"""Builds the "Berlin Marathon" GPX used for the Berlin race-week figures.

The route follows real streets along the outline of the BMW Berlin Marathon
course (Straße des 17. Juni → Moabit → Mitte → Friedrichshain → Kreuzberg →
Neukölln → Schöneberg → Steglitz/Wilder Eber → Kurfürstendamm → Potsdamer
Platz → Unter den Linden → Brandenburg Gate). It is an illustration, not the
certified course: waypoints are routed with the public OSM foot router, so a
few corners differ from the real line.

Timing: a 3:57 finish with a small negative split (5:40 /km for the first
half, 5:35 after), a short slow-down at the km 33 drink station, and a heart
rate that drifts upwards. Date: the 2025 race day, so the app accepts it as a
past run.

Import it like the Central Park loop (see make-central-park-loop.py).
Usage: python3 make-berlin-marathon.py [--refetch]
"""
import bisect, json, math, os, random, sys, urllib.request
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'berlin-marathon-route.json')
OUT = os.path.join(HERE, 'berlin-marathon.gpx')

# (lat, lon) in course order
WAYPOINTS = [
    (52.51405, 13.37050),  # start, Straße des 17. Juni
    (52.51450, 13.35010),  # Großer Stern
    (52.51900, 13.34780),  # Spreeweg
    (52.52330, 13.34700),  # Alt-Moabit
    (52.52300, 13.36000),  # Alt-Moabit east
    (52.52580, 13.37300),  # Invalidenstraße
    (52.52750, 13.38750),  # Oranienburger Tor
    (52.52960, 13.40150),  # Rosenthaler Platz
    (52.52700, 13.41050),  # Rosa-Luxemburg-Platz
    (52.52350, 13.41900),  # Mollstraße
    (52.51800, 13.43300),  # Strausberger Platz
    (52.51150, 13.42600),  # Lichtenberger Straße
    (52.50700, 13.41600),  # Heinrich-Heine-Straße
    (52.50350, 13.41050),  # Moritzplatz
    (52.49900, 13.41800),  # Kottbusser Tor
    (52.48680, 13.42450),  # Hermannplatz
    (52.48850, 13.41300),  # Hasenheide
    (52.48950, 13.40780),  # Südstern
    (52.49150, 13.39200),  # Gneisenaustraße
    (52.49300, 13.38800),  # Mehringdamm
    (52.49280, 13.38100),  # Yorckstraße
    (52.48950, 13.35900),  # Kleistpark
    (52.48500, 13.35300),  # Hauptstraße
    (52.47870, 13.34300),  # Innsbrucker Platz
    (52.46500, 13.32800),  # Walther-Schreiber-Platz
    (52.45700, 13.32100),  # Schloßstraße
    (52.45480, 13.32000),  # Rathaus Steglitz
    (52.45300, 13.31700),  # Albrechtstraße
    (52.46430, 13.30300),  # Wilder Eber
    (52.47800, 13.30700),  # Hohenzollerndamm
    (52.49000, 13.31400),  # Fehrbelliner Platz
    (52.49500, 13.30650),  # Konstanzer Straße
    (52.49990, 13.30700),  # Adenauerplatz
    (52.50050, 13.31700),  # Olivaer Platz
    (52.50450, 13.33500),  # Breitscheidplatz
    (52.50190, 13.34310),  # Wittenbergplatz
    (52.49850, 13.35900),  # Bülowstraße
    (52.50300, 13.36700),  # Potsdamer Straße
    (52.50940, 13.37600),  # Potsdamer Platz
    (52.51000, 13.38900),  # Leipziger Straße
    (52.51100, 13.40350),  # Spittelmarkt
    (52.51250, 13.39800),  # Hausvogteiplatz
    (52.51360, 13.39270),  # Gendarmenmarkt
    (52.51700, 13.38900),  # Unter den Linden
    (52.51630, 13.37770),  # Brandenburg Gate
    (52.51450, 13.37150),  # finish
]


def dist(a, b):
    la1, lo1 = a; la2, lo2 = b
    x = (lo2 - lo1) * math.cos(math.radians((la1 + la2) / 2)) * 111320
    y = (la2 - la1) * 110574
    return math.hypot(x, y)


def fetch_route():
    route = []
    for a, b in zip(WAYPOINTS, WAYPOINTS[1:]):
        url = ('https://routing.openstreetmap.de/routed-foot/route/v1/driving/'
               f'{a[1]},{a[0]};{b[1]},{b[0]}?overview=full&geometries=geojson')
        req = urllib.request.Request(url, headers={'User-Agent': 'irunning-blog-figures/1.0'})
        data = json.loads(urllib.request.urlopen(req, timeout=60).read())
        pts = [(la, lo) for lo, la in data['routes'][0]['geometry']['coordinates']]
        route += pts if not route else pts[1:]
    return despur(route)


def despur(route):
    # The router walks to a waypoint that sits beside the road and back again.
    # Cut those out-and-back spurs: a point that the route revisits shortly after.
    out, i = [], 0
    while i < len(route):
        out.append(route[i])
        run, j, cut = 0.0, i + 1, None
        while j < len(route) and run < 800:
            run += dist(route[j - 1], route[j])
            if run > 30 and dist(route[i], route[j]) < 8:
                cut = j
            j += 1
        i = cut + 1 if cut else i + 1
    return out


def write_gpx(route):
    cum = [0.0]
    for a, b in zip(route, route[1:]):
        cum.append(cum[-1] + dist(a, b))
    L = cum[-1]
    # GPS distance of a real marathon runs a little long; keep the time maths
    # on the certified 42,195 m.
    scale = 42195 / L

    def pace(km):
        p = 340 if km < 21.1 else 335
        if 32.9 <= km < 33.2:
            p = 420  # drink station
        return p

    random.seed(27)
    t0 = datetime(2025, 9, 21, 7, 11, 0, tzinfo=timezone.utc)
    pts, m, t, hr = [], 0.0, 0.0, 120.0
    while m < L:
        km = m * scale / 1000
        hr_t = 138 + km * 0.32 + (5 if km > 38 else 0)
        hr += (hr_t - hr) * 0.08 + random.uniform(-1.0, 1.0)
        i = min(bisect.bisect_right(cum, m) - 1, len(route) - 2)
        f = (m - cum[i]) / max(1e-6, cum[i + 1] - cum[i]); a, b = route[i], route[i + 1]
        la = a[0] + (b[0] - a[0]) * f + random.gauss(0, 0.4e-5)
        lo = a[1] + (b[1] - a[1]) * f + random.gauss(0, 0.6e-5)
        # Berlin is flat: 34–52 m, a few gentle rises (Kreuzberg, Steglitz).
        ele = 36 + 6 * math.sin(km / 4.3) + 5 * math.exp(-((km - 27) / 3) ** 2) + 3 * math.exp(-((km - 17) / 2) ** 2)
        pts.append((t, la, lo, int(round(hr)), ele))
        m += 5.0 / (pace(km) / 1000.0) / scale; t += 5.0
    iso = lambda s: (t0 + timedelta(seconds=s)).strftime('%Y-%m-%dT%H:%M:%SZ')
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<gpx version="1.1" creator="iRunning blog" xmlns="http://www.topografix.com/GPX/1/1" '
             'xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">',
             f' <metadata><time>{iso(0)}</time></metadata>',
             ' <trk><name>Berlin Marathon</name><type>running</type><trkseg>']
    for t, la, lo, h, ele in pts:
        lines.append(f'  <trkpt lat="{la:.7f}" lon="{lo:.7f}"><ele>{ele:.1f}</ele><time>{iso(t)}</time><extensions>'
                     f'<gpxtpx:TrackPointExtension><gpxtpx:hr>{h}</gpxtpx:hr></gpxtpx:TrackPointExtension></extensions></trkpt>')
    lines.append(' </trkseg></trk></gpx>')
    open(OUT, 'w').write('\n'.join(lines))
    print(f'{OUT}: route {L:.0f} m, {int(t // 3600)}:{int(t % 3600 // 60):02d}:{int(t % 60):02d}, {len(pts)} points')


if __name__ == '__main__':
    if '--refetch' in sys.argv or not os.path.exists(CACHE):
        route = fetch_route()
        json.dump(route, open(CACHE, 'w'))
    else:
        route = [tuple(p) for p in json.load(open(CACHE))]
    write_gpx(route)
