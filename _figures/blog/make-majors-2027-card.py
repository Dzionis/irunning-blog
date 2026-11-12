#!/usr/bin/env python3
"""Builds majors-2027-card.html: the 2027 World Marathon Majors calendar card
(1080x1350, Instagram 4:5) in the site's Trail calm style.

Profiles come from gpx/majors-2027-profiles.json: elevation sampled every 150 m
along each course line (USGS NED 10 m for the US races, EU-DEM 25 m for London
and Berlin, ASTER/SRTM 30 m for Tokyo and Cape Town, the official 2025 course
file for Sydney), smoothed, with the NYC bridge decks put back and the Cape Town
route-line detour over Military Rd replaced by the flat Buitengracht St line.
All eight are drawn to ONE vertical scale, so a flat course looks flat.

Render (from _figures/blog):
  python3 make-majors-2027-card.py && "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
    --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1080,1350 --allow-file-access-from-files \
    --screenshot=../../assets/images/blog/majors-2027-card.png "file://$PWD/majors-2027-card.html"
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
prof = json.load(open(os.path.join(HERE, "gpx/majors-2027-profiles.json")))

# key, city, official name, tag, date, weekday, plan start, route, status, status kind, climb m
RACES = [
    ("tokyo", "Tokyo", "Tokyo Marathon", None, "7 Mar", "Sunday", "16 Nov", "Lottery", "Closed", "closed", 60),
    ("boston", "Boston", "Boston Marathon", None, "19 Apr", "Monday", "28 Dec", "Qualify", "Closed · charity later", "closed", 248),
    ("london", "London", "TCS London Marathon", "Two days", "24–25 Apr", "Sat & Sun", "4 Jan", "Ballot", "Closed · charity open", "closed", 127),
    ("cape-town", "Cape Town", "Sanlam Cape Town Marathon", "New Major", "23 May", "Sunday", "1 Feb", "Lottery", "Closed · charity open", "closed", 205),
    ("sydney", "Sydney", "TCS Sydney Marathon", None, "29 Aug", "Sunday", "10 May", "Ballot", "Closed · charity open", "closed", 262),
    ("berlin", "Berlin", "Generali Berlin Marathon", "New name", "26 Sep", "Sunday", "7 Jun", "Lottery", "Results Thu 3 Dec", "pending", 73),
    ("chicago", "Chicago", "Bank of America Chicago Marathon", None, "10 Oct", "Sunday", "21 Jun", "Drawing", "Results Tue 8 Dec", "pending", 74),
    ("new-york", "New York City", "TCS New York City Marathon", None, "7 Nov", "Sunday", "19 Jul", "Drawing", "Expected Feb 2027", "soon", 294),
]

SW, SH = 120, 54           # sparkline box
RANGE_M = 125              # metres that fill SH: Boston's ~120 m drop is the largest

def spark(key):
    km, ele = prof[key]["km"], prof[key]["ele"]
    lo, L = min(ele), km[-1]
    pts = [(x / L * SW, SH - 2 - (e - lo) / RANGE_M * (SH - 4)) for x, e in zip(km, ele)]
    line = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = line + f" L{SW},{SH} L0,{SH} Z"
    return (f'<svg width="{SW}" height="{SH}" viewBox="0 0 {SW} {SH}">'
            f'<path d="{area}" fill="#E1F5EE"/><path d="{line}" fill="none" stroke="#1D9E75" stroke-width="2.4" '
            f'stroke-linejoin="round" stroke-linecap="round"/></svg>')

rows = []
for key, city, name, tag, date, wd, plan, route, status, kind, climb in RACES:
    tag_html = f'<span class="tag">{tag}</span>' if tag else ""
    rows.append(f'''
  <div class="row">
    <div class="c-date"><div class="d">{date}</div><div class="wd">{wd}</div></div>
    <div class="c-race"><div class="city">{city}{tag_html}</div><div class="name">{name}</div></div>
    <div class="c-entry"><span class="pill">{route}</span><div class="st {kind}"><i></i>{status}</div></div>
    <div class="c-climb">{spark(key)}<div class="m"><b>{climb}</b> m<span>{round(climb * 3.28084)} ft</span></div></div>
    <div class="c-plan">{plan}</div>
  </div>''')

html = f'''<!doctype html><html><head><meta charset="utf-8">
<style>
:root {{
  --green-50:#E1F5EE; --green-100:#9FE1CB; --green-400:#1D9E75; --green-600:#0F6E56; --green-900:#04342C;
  --paper-100:#F8F6EF; --paper-200:#F1EFE8; --paper-300:#E4E2DA; --paper-400:#D3D1C7; --paper-600:#888780;
  --paper-800:#444441; --paper-900:#2C2C2A; --amber-50:#FAEEDA; --amber-400:#BA7517; --amber-600:#854F0B; --mut:#6E7B74;
}}
* {{ box-sizing:border-box; margin:0; padding:0; }}
html, body {{ width:1080px; height:1350px; background:var(--paper-200); overflow:hidden; }}
body {{ font-family:-apple-system, BlinkMacSystemFont, "Inter", sans-serif; color:var(--paper-900);
  -webkit-font-smoothing:antialiased; font-variant-numeric:tabular-nums; }}
.canvas {{ width:1080px; height:1350px; padding:54px 48px 0; position:relative; }}
.brand {{ display:flex; align-items:center; gap:14px; }}
.brand img {{ width:46px; height:46px; border-radius:11px; }}
.brand span {{ font-size:25px; font-weight:600; color:var(--green-900); letter-spacing:-0.01em; }}
.brand .chip {{ margin-left:auto; font-size:15px; font-weight:600; letter-spacing:.1em; text-transform:uppercase;
  color:var(--amber-600); background:var(--amber-50); padding:9px 16px; border-radius:999px; }}
h1 {{ font-size:68px; line-height:1.02; font-weight:600; color:var(--green-900); letter-spacing:-0.025em; margin:28px 0 12px; }}
.sub {{ font-size:22px; line-height:1.4; color:var(--paper-800); max-width:900px; }}
.card {{ margin-top:30px; background:#fff; border-radius:28px; border:1px solid var(--paper-400); padding:4px 24px 6px; }}
.row, .head {{ display:grid; grid-template-columns:148px 252px 190px 1fr 104px; align-items:center; column-gap:10px; }}
.head {{ height:52px; font-size:13.5px; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--mut);
  border-bottom:1px solid var(--paper-400); }}
.head .r {{ text-align:right; white-space:nowrap; }}
.row {{ height:98px; border-bottom:1px solid var(--paper-300); }}
.row:last-child {{ border-bottom:0; }}
.d {{ font-size:28px; font-weight:600; color:var(--green-900); letter-spacing:-0.01em; white-space:nowrap; }}
.wd {{ font-size:15px; color:var(--mut); margin-top:3px; }}
.city {{ font-size:27px; font-weight:600; color:var(--green-900); letter-spacing:-0.01em; display:flex; align-items:center; gap:10px; }}
.tag {{ font-size:12px; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:var(--green-600);
  background:var(--green-50); padding:4px 9px; border-radius:999px; }}
.name {{ font-size:15px; color:var(--mut); margin-top:4px; white-space:nowrap; }}
.pill {{ display:inline-block; font-size:16px; font-weight:600; color:var(--green-900); background:var(--paper-200);
  border:1px solid var(--paper-400); padding:5px 13px; border-radius:999px; }}
.st {{ font-size:15.5px; color:var(--paper-800); margin-top:8px; display:flex; align-items:center; gap:8px; white-space:nowrap; }}
.st i {{ width:9px; height:9px; border-radius:50%; background:var(--paper-600); flex:none; }}
.st.pending {{ color:var(--amber-600); font-weight:600; }} .st.pending i {{ background:var(--amber-400); }}
.st.soon {{ color:var(--green-600); font-weight:600; }} .st.soon i {{ background:var(--green-400); }}
.c-climb {{ display:flex; align-items:flex-end; gap:12px; }}
.c-climb svg {{ flex:none; display:block; }}
.m {{ font-size:17px; color:var(--paper-800); line-height:1.1; white-space:nowrap; }}
.m b {{ font-size:27px; font-weight:600; color:var(--green-900); }}
.m span {{ display:block; font-size:14px; color:var(--mut); margin-top:3px; }}
.c-plan {{ text-align:right; font-size:19px; font-weight:600; color:var(--green-600); white-space:nowrap; }}
.legend {{ display:flex; gap:26px; margin:20px 4px 0; font-size:15.5px; color:var(--paper-800); }}
.legend span {{ display:flex; align-items:center; gap:8px; }}
.legend i {{ width:9px; height:9px; border-radius:50%; background:var(--paper-600); }}
.foot {{ position:absolute; left:48px; right:48px; bottom:36px; display:flex; align-items:flex-end; gap:30px; }}
.foot p {{ font-size:14px; line-height:1.45; color:var(--mut); flex:1; }}
.foot .url {{ font-size:20px; font-weight:600; color:var(--green-900); white-space:nowrap; }}
</style></head><body><div class="canvas">
  <div class="brand"><img src="../../assets/images/icon.png" alt=""><span>iRunning</span><div class="chip">As of 16 Nov 2026</div></div>
  <h1>World Marathon<br>Majors 2027</h1>
  <p class="sub">Race days, entry status, course climb and when a 16-week plan starts.</p>
  <div class="card">
    <div class="head"><div>Race day</div><div>Race</div><div>Entry</div><div>Climb</div><div class="r">Plan from</div></div>{"".join(rows)}
  </div>
  <div class="legend">
    <span><i></i>Closed</span><span><i style="background:var(--amber-400)"></i>Results pending</span><span><i style="background:var(--green-400)"></i>Coming up</span>
  </div>
  <div class="foot">
    <p>Climb: total ascent per FindMyMarathon (Sydney’s organiser gives 313 m for 2026). Profiles share one vertical scale,
      from elevation data along each course. Plan from: Monday that week 1 of a 16-week plan starts. Check official sites before entering.</p>
    <div class="url">irunning.app</div>
  </div>
</div></body></html>
'''
open(os.path.join(HERE, "majors-2027-card.html"), "w").write(html)
print("wrote majors-2027-card.html")
