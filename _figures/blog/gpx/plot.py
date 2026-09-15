import re, sys, json
src, out = sys.argv[1], sys.argv[2]
pts = re.findall(r'<trkpt lon="([-\d.]+)" lat="([-\d.]+)"', open(src).read())
coords = [[float(la), float(lo)] for lo, la in pts]
html = f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"><script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>html,body,#m{{margin:0;width:900px;height:900px}}</style></head><body><div id="m"></div><script>
const c={json.dumps(coords)}; const m=L.map('m',{{zoomControl:false}}); L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png').addTo(m);
const l=L.polyline(c,{{color:'#D85A30',weight:4}}).addTo(m); m.fitBounds(l.getBounds().pad(0.08));
L.circleMarker(c[0],{{radius:6,color:'#04342C'}}).addTo(m);
</script></body></html>'''
open(out,'w').write(html)
