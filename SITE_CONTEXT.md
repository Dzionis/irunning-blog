# Site Context — iRunning Website

Use this document when making decisions about content, design, SEO, analytics, or development for this project.

---

## The App

- **Name:** iRunning: Run Tracker & Coach
- **Platform:** iOS (iPhone + Apple Watch, widgets)
- **App Store ID:** 6770997508 (bundle `interval.irunning`)
- **App Store URL:** https://apps.apple.com/us/app/id6770997508
- **Core features:**
  - Custom interval workout builder (work/rest/warmup/cooldown, time/distance/open goals, repeat blocks)
  - Workout templates (Tabata, HIIT, tempo, fartlek, pyramid, progression)
  - GPS run tracking with route maps and per-interval splits
  - Voice cues + countdown beeps with music ducking
  - Apple Watch app (standalone, haptics, heart rate)
  - Heart rate zones (live + time-in-zone)
  - Training plans: Start Walking (free), 0→5K, 5K→10K, Weight Loss Kickstart
  - Live Activity / Dynamic Island
  - Import from Apple Health, GPX, FIT (v1.1.1)
  - 17+ share card templates incl. transparent photo overlays (v1.1.1)
  - Apple Health integration, GPX/FIT export
- **Monetisation:** freemium subscription (via Apphud)
- **Target users:** interval runners, couch-to-5K beginners, Apple Watch runners, data-loving hobbyists
- **App source:** `/Users/dzionis/Documents/home/irunning-ios` (ASO copy in `ASO_LOCALIZATIONS.md`)

---

## The Website

- **URL:** https://irunning.app
- **Purpose:** Marketing + SEO blog for the iOS app. Goal: organic search traffic → App Store installs.
- **Tech stack:** Jekyll (static), same architecture as the `tts-blog` project
- **Hosting:** Static (GitHub Pages intended; `CNAME` present)
- **CSS:** Custom `assets/css/main.css` — web port of the app's "Trail calm" design system
- **Fonts:** system stack first (`-apple-system` → SF Pro on Apple devices, per design system), Inter 400/500/600 from Google Fonts as cross-platform fallback
- **Plugins:** jekyll-seo-tag, jekyll-feed (sitemap is a manual template at `/sitemap.xml`)

---

## Design System (web port of "Trail calm")

Source of truth: `DESIGN_SYSTEM.md` (copied from the app repo). Web decisions:

- **Light mode only** ("daylight first" — dark mode deliberately not implemented yet)
- Page bg `#F1EFE8` (paper/200), cards `#FFFFFF`, borders `#D3D1C7`
- Text: headings `#04342C` (green/900), body `#2C2C2A` (paper/900), secondary `#888780`
- Accent `#1D9E75` (green/400), hover/pressed `#0F6E56` (green/600)
- **No gradients** (flat paper), **no weight 700+** (400/500/600 only)
- Soft green-tinted shadows (`--shadow-sm` / `--shadow-md`) only for lift on hover and the hero pill; surfaces stay flat at rest. Header gets its hairline + shadow only after scrolling (`.is-scrolled`, `site.js`)
- Radii: 6 / 12 / 20 / 28 / 999 px (sm/md/lg/xl/full)
- Stats/numbers use tabular numerics (`font-variant-numeric: tabular-nums`)
- Category tag colors mirror the app's interval states:
  - `features` → green (work), `events` → amber (warmup), `releases` → coral (cooldown), `news` → neutral paper (rest)
- Hero, Watch section, and the "From First Step to Finish Line" gallery use **real simulator screenshots** in CSS device frames (`.phone`/`.phone-screen-shot`, `.watch-body`/`.watch-screen`, `.shot-frame`)

## Regenerating app screenshots

**Hero (since 2026-10-27):** three fanned phones — `hero-plan.webp` (0→5K plan overview, week 3) · `hero-run.webp` (run screen) · `hero-summary.webp` ("Tuesday 400s" run summary), from app commit `859eb92` (1.2.4) on the "iRunning Blog Shots" simulator. Run screen without tapping: `xcrun simctl launch <udid> interval.irunning --debug-run-display classic --target hr --hr 158 --elapsed 31 --real-map --route-gpx <container>/tmp/cp.gpx --route-km 3.2` (copy `_figures/blog/gpx/central-park-loop.gpx` into the app's data container `tmp/` first). Plan + summary: launch with `--seed-share-run --seed-home-block active`, Home › "Open plan", then History › Tuesday 400s. The app reads its own `settings.appearanceMode` (set it to `light`, see the rucking note below); status bar `--batteryState discharging` hides the charging bolt. Encode with `cwebp -q 88 -resize 644 0` (run) / `-q 85 -resize 560 0` (sides). The Xcode project is git-ignored in the app repo, so a clean build from `git archive HEAD` needs `irunning.xcodeproj` and `StravaCredentials.swift` copied from the working tree. Fan geometry lives in `.hero-phones` / `.phone-side` in `main.css`. The older single `screen-run.png` is still the JSON-LD screenshot.

Screens live in `assets/images/screens/` (screen-run, screen-plan, screen-summary, screen-celebrate, screen-share @ ~460–644px wide; screen-watch @ 416px). To refresh after app updates:

1. Build `irunning` scheme for an iPhone simulator, `iRunningWatch` for a watch simulator (see the app repo)
2. Skip onboarding: `xcrun simctl spawn <udid> defaults write interval.irunning settings.hasCompletedOnboarding -bool YES`
3. Marketing status bar: `xcrun simctl status_bar <udid> override --time "9:41" --batteryLevel 100 --cellularBars 4 --wifiBars 3`
4. Launch with debug seeds: `xcrun simctl launch <udid> interval.irunning --seed-share-run --seed-home-block active` — seeds the "Tuesday 400s" run (full HR/route/splits) and an active 0→5K plan with premium override
5. Live run screen: `xcrun simctl location <udid> run "City Run"`, start the plan session, skip the warm-up (hold Skip), wait for the work-interval ring to deplete
6. Watch: launch `interval.irunning.watchkitapp` standalone; watch sim generates real HR; the workout list has "Tuesday 400s" built in
7. Capture: `xcrun simctl io <udid> screenshot file.png`, downscale with `sips -Z 1000` (hero: 1400)
8. OG image: scratch `og.html` renders the hero screenshot in a frame via headless Chrome at 1200×630

---

## Site Structure

Design source (Claude Design project 019e0c54-cd1a-7445-8570-08cbde57e111): hero badge + "Your session" strip come from variant **V4 · Dimensional** in `Site - Main Page Variants.html` (V4's green disc was later removed in favor of a soft phone shadow); the watch card surface + CSS Apple Watch Ultra render (`.aw-*` classes) come from variant **A · Floating display** in `Site - Watch Block Variants.html`. The watch screen image is the simulator capture center-cropped to 401×496 (true display ratio), matching the design's `assets/watch-screen.png`.

```
/               — Homepage: hero ("New" pill → latest `releases` post, 4.9 / 41 plans / Free stats row, real run screenshot), "Your session" strip, blog (1 featured + 3 compact cards with image previews, #blog), features (#features), Watch (#watch), screens gallery (#screens), import/share, reviews, CTA
/blog/          — Blog listing: newest post as a wide featured card, then a 3-column grid; category filter chips (counts), deep-linkable as /blog/#training
/blog/:year/:month/:title/  — Individual posts: breadcrumb, author/date/read-time row, reading-progress bar, dark CTA, "Keep reading" (3 cards, same category first)
/privacy/       — Privacy policy (covers GPS + HealthKit data; lists Firebase, Amplitude, Apphud, Facebook SDKs)
/terms/         — Terms of service (incl. health/fitness disclaimer, subscriptions)
/sitemap.xml    — manual Liquid template
/robots.txt
```

### Templates / Layouts

| File | Purpose |
|---|---|
| `_layouts/default.html` | Base layout (header + footer + scripts) |
| `_layouts/post.html` | Blog post layout with end-of-post CTA |
| `_layouts/page.html` | Static pages (privacy, terms) |
| `_includes/header.html` | Site header (icon + iRunning, nav: Features, Apple Watch — hidden under 768px — Blog, Get App) |
| `_includes/footer.html` | Dark green footer: brand + download button, App / Blog (category deep links) / Legal columns |
| `_data/social.yml` | Official social profiles (all **@irunningapp**: Instagram, TikTok, YouTube, Threads, X, Facebook, Pinterest) with Simple Icons paths; footer icon row + homepage JSON-LD `sameAs`. Keep `_config.yml` `social.links` (jekyll-seo-tag sameAs) in sync |
| `_includes/post-card.html` | Blog card with image preview; `variant` featured / compact; used by homepage, listing, "Keep reading" |
| `_includes/seo-head.html` | jekyll-seo-tag + smart app banner (`apple-itunes-app` id 6770997508) + favicon |
| `_includes/analytics.html` | GA4 gtag.js — auto-disabled while ID is the `G-XXXXXXXXXX` placeholder |

---

## Analytics Setup

- **GA4 Measurement ID:** `G-LZY2M1LLF5` (set 2026-08-21) — web data stream "iRunning website" on the app's Firebase GA4 property `irunning-4d1b0`, which is already linked to Google Ads account **654-344-4532**.
- Event tracking is data-attribute driven (same system as tts-blog): `data-ga-event`, `data-ga-location`, `data-ga-destination`, handled by delegation in `assets/js/analytics.js`.
- **App Store campaign tokens:** `analytics.js` rewrites every `apps.apple.com` link at runtime with `ct=<token>&mt=8` — `ct=pmax` for sessions arriving with `gclid`/`utm_medium=cpc` (persisted in sessionStorage), `ct=website` otherwise. `pt=` (Apple provider token) not added yet — required before App Store Connect App Analytics will report these campaigns; web-referrer attribution works regardless.

### Advertising (2026-08)

- **Google Ads PMax campaign** (free credits): goal = GA4 `app_store_click` imported as primary conversion; final URL `https://irunning.app`, URL expansion OFF. Ad copy asset pack drafted 2026-08-21 (15 headlines / 5 long / 5 descriptions, verified ≤30/90 chars).
- A Google **App campaign** (5×30 headlines / 5×90 descriptions format) was also drafted for App Store installs.

### Custom events wired

| Event | Where |
|---|---|
| `hero_cta_click` | Hero "Download on App Store" |
| `cta_click` | Homepage bottom CTA "Start Running — Free" |
| `footer_cta_click` | End-of-post CTA |
| `app_store_click` | Header "Get App", footer "App Store" (also auto-fired alongside any event whose destination is apps.apple.com) |
| `blog_post_click` | Blog cards (`homepage_blog_preview`, `blog_listing`, `post_related`) |
| `release_pill_click` | Hero "New · iRunning x.y.z" pill |
| `social_click` | Footer social icons (`data-ga-destination` = profile URL) |
| `scroll_90` | 90% scroll depth |

---

## Blog Content

**Categories (fixed set, color-coded):**

| Category | Use for | Color |
|---|---|---|
| `features` | App functionality, benefit-focused, no tech details | green |
| `events` | Races, marathon calendars, running events | amber |
| `news` | Running-world news and trends | neutral |
| `releases` | App version announcements (source: `ASO_LOCALIZATIONS.md` What's New) | coral |
| `guides` | How-to posts: step-by-step use of a feature (Siri, Action Button, share overlays) | muted grey-green |
| `training` | Training guides built around a plan or method (Sub-30, Japanese Walking, zone 2) | teal |

**8 launch posts** (May–Aug 2026, biweekly): interval builder, Apple Watch, heart rate zones, voice cues, training plans, 2026 running trends, autumn 2026 marathon calendar (Berlin Sep 27 / Chicago Oct 11 / NYC Nov 1 — verified Aug 2026), v1.1.1 release notes.

**Sep 2026 how-to posts** (iRunning 1.2 App Intents, facts taken from `irunning-ios/irunning/AppIntents/`): Siri phrases + Shortcuts actions (`siri-shortcuts-hands-free-running`), "Announce my run" on the Action Button / Back Tap / Control Center (`action-button-announce-my-run`). The two cross-link via `post_url`. Re-check them if intent phrases, the announce settings path (Settings › Customise › Run screen › What to announce) or the iOS 18 minimum change.

**Card previews.** Every post needs `image: path:` in front matter — it is both the OG image and the card preview. Cards load a 720px WebP from `assets/images/blog/thumbs/<image basename>.webp` when it exists (else the full image, else a flat ring cover in the category colour). After adding a post, run `scripts/make-blog-thumbs.sh` (needs `cwebp`; `--force` rebuilds all) and commit the new thumb. The eight launch posts (May–Aug) borrow app-screen figures from later posts as their image.

**Post figures** live in `assets/images/blog/` (PNG @2x, 1440px wide + a 800px `-mobile` variant served via `<picture>` under 560px, because text in a 720px figure is unreadable at phone width). Styled by `.post-figure` in `main.css`. Sources are HTML pages in `_figures/blog/` (Jekyll ignores the folder); re-render one with `_figures/blog/render.sh <name>` (headless Chrome, height read from `.canvas`). The app screens inside them (`announce.png`, `run-classic.png`, `run-locked.png`) were captured without any tapping via the app's DEBUG launch flag: `xcrun simctl launch <udid> interval.irunning --debug-run-display announce` (also `classic --target hr`, `classicLock --locked`, `pickerRun`, `pickerLocked`; see `RunDisplayDebugScreen.swift`). Launch iRunning right after another app and iOS adds a "◂ Settings" back-link to the status bar, so terminate other apps first.

**1.2.2 posts.** iRunning 1.2.2 reached the App Store on 2026-09-16; the six posts that depended on it went live the same day: `zone-2-running-aerobic-base` (dated 09-06), `japanese-walking-interval-walk` (09-09), `treadmill-intervals-indoor-running` (09-10), `sub-30-5k-training-plan` (09-12), `run-video-instagram-stories-tiktok` (09-14) and the release post `irunning-1-2-2-run-videos-plans-dark-mode` (dated 09-16, the release day). Dates were deliberately set in the past (2026-09-15 decision) so the blog reads as a steady cadence. The same pattern applies to the next version: write posts early with `published: false`, preview them on the drafts server, and drop the flag on release day. The 1.2.0-era how-to posts are live and dated 08-27 / 09-01 / 09-03 / 09-05 (1.2.0 reached the store ~08-30, 1.2.1 ~09-10). The AI builder post (09-07) uses only the input screen plus a diagram: on-device generation does not work in the simulator (FoundationModels reports the model catalog has no assets), so there is no real preview screenshot — the diagram's result card follows the generator's own rules in `AIWorkoutGenerator.swift` (5-min warm-up/cool-down, repeat groups). Import facts (Health/GPX/FIT, auto-import 90 days + 7-day overlap, 7-day free window) come from `irunning/Features/ImportRuns/`; treadmill facts (Indoor picker, fixed 4 m/s distance estimate, 8 presets, Winter Treadmill Plan) from `WorkoutPreset.swift`, `RunEnvironmentPicker.swift`, `PlanCatalog+Treadmill.swift`. Preview them locally with the `irunning-site-drafts` launch config (`jekyll serve --unpublished`, port 4001). Never `post_url`-link a published post to a hidden one: the build fails.

**More figure recipes (Sep 2026).**
- Photo-heavy composites opt into JPEG with `<html data-format="jpg">`; `render.sh` converts them. Screenshots and photo backgrounds they use live in `_figures/blog/src/`.
- Real app screens beyond the run display need taps. Seed data first: `xcrun simctl launch <udid> interval.irunning --seed-share-run --seed-share-walk --seed-home-block active --debug-brand-tiles` ("Tuesday 400s", Berlin loop, full HR; brand tiles force the Instagram/TikTok buttons on a simulator).
- Transparent overlay PNGs (1080×1920, alpha): in the share picker tap the nav-bar **Share** on an overlay, then collect `tmp/*-story.png` from `xcrun simctl get_app_container <udid> interval.irunning data`.
- Run videos: Share › Video › Export video writes `tmp/irun-…-video-story.mp4` in the same container. The seed run's route is synthetic and cuts through buildings, so the video figures use an imported real route instead: `_figures/blog/gpx/make-central-park-loop.py` builds a GPX along Central Park's drives (Overpass geometry + drive-only Dijkstra, timed with a pace plan and heart rate); drop it into the simulator's Files storage (`…/Shared/AppGroup/<group.com.apple.FileProvider.LocalStorage>/File Provider Storage/`) and import it via History › import › "GPX or FIT file" › Browse › On My iPhone. Run name "Central Park Loop", 10.7 km, 56:00. Frames were pulled with an AVFoundation Swift script, and the web copy re-encoded to 540×960 H.264 at 1.4 Mbps (~2.1 MB for 12 s) because Homebrew ffmpeg is broken on this machine. Don't go lower: 800 kbps already softened the satellite map and small caps noticeably. Embedded as a plain `<video autoplay muted loop playsinline>` in `.post-figure.video-figure` (40px vertical margins, 320px wide, rounded corners). A stories-style phone mock was tried on 2026-09-15 and removed on request: keep it plain. `.post-figure video` must keep `height: auto` — the `height` attribute otherwise letterboxes the 320px-wide video to 960px tall. The `src` carries a `?v=YYYYMMDD` query: bump it whenever the MP4 is replaced at the same path, or browsers keep a cached (possibly truncated) copy and report a format error.
- **Berlin Marathon series (Sep 2026).** Four posts dated back: `share-berlin-marathon-finish` (09-04), `negative-split-marathon-pacing` (09-08), `marathon-taper-last-two-weeks` (09-13), `berlin-marathon-course-guide` (09-15). Race facts came from bmw-berlin-marathon.com (wave starts from 08:45, 6:15 limit, expo at Tempelhof Thu–Sat, drink stations at fixed km, Maurten gel only at km 27.5, open-ear headphones only) — re-check them each year. `_figures/blog/gpx/make-berlin-marathon.py` builds an illustrative 42.2 km GPX along the course outline: waypoints routed with the public OSM foot router (`routing.openstreetmap.de/routed-foot`), a despur pass removes the router's out-and-back detours, and the pace plan is a 3:57:45 negative split with a slow km at the km 33 drink station. It is *not* the certified course — never label it as one. The app smooths a GPX, so its measured distance lands ~2% under the file's geometry: the route is deliberately ~43.2 km so the summary reads 42.4 km, which is also what a real watch shows. Imported as "Berlin Marathon" (a GPX keeps its track name; FIT/Health imports don't, and runs cannot be renamed in the app). Screens in `_figures/blog/src/berlin-*.jpg`; the Apple Weather card fills in the real 21 Sep 2025 conditions (24 °C), which is why the file uses that date.
- Durations of an hour or more used to render as "237:45" (`formatSeconds` in the app had no hours). The fix landed in the app while these posts were written, so the marathon screenshots were taken from a local build of that branch — a store build before the fix still shows the old format.
- **First marathon post (2026-09-22).** `first-marathon-training-plan-16-weeks` mirrors the half marathon post, with facts from `PlanCatalog+Distance.swift` (`marathon`: 16 wk × 4, long run in minutes × 155 m, capped at 2 h 45 m). The plan is "Advanced" and asks for a finished half, so the post says "first marathon", never "beginner runner". Hero `first-marathon-hero.jpg` is a Gemini photo (prompt in `PROMPTS.md`; "Copy image" gave 1024×687, not 1264×848). The long-run chart is `marathon-long-run` (SVG bars written by hand into the figure HTML, same style as `berlin-taper-volume`).
- **Plan screens (2026-09-21).** `marathon-plan-screens` (overview + week 10) and, for the recovery post `after-marathon-recovery-first-two-weeks` (dated 2026-09-29, evergreen, no race results in it), `recovery-plan-screens` (overview + week 1) and `recovery-effort-screen` (reuses `src/berlin-recovery.jpg`). Shot on the "iRunning Blog Shots" simulator: launch with `--seed-share-run --seed-home-block noPlan`, Home › Browse all 41 plans. Paid plans open because Settings › Debug › Enable premium is on in that simulator (the `--seed-home-block` states flip it, so check it after seeding). Marathon is the last card of Race distances, Post-Race Recovery the last of Comebacks; expand a week by tapping its header. Scroll with slow drags that hold still at the end, a plain swipe flings the list to the bottom.
- **Berlin 2026 results post (2026-09-27).** `berlin-marathon-2026-results`: results and splits from live coverage (marathonhandbook, world-track, Yahoo) on race day, re-check against the official results. Hero `berlin-2026-winners` pairs two Wikimedia Commons photos from *earlier* Berlin editions (Assefa 2023 by IgorCalzone1, CC BY-SA 4.0; Adola 2025 by Leonhard Lenz, CC0), credited in the figcaption — keep that credit whenever the image is reused. Real athletes appear only in licensed photos, never in generated ones.
- **Rucking post (2026-10-14).** `rucking-for-beginners-first-8-weeks` (training, dated 2026-10-15; hero `rucking-hero.jpg` is a Gemini photo, prompt in `PROMPTS.md`). Facts from `PlanCatalog+Hiking.swift` (`ruck`: 8 wk × 3, Base 4 · Build 3 · Peak 1, loaded walks are zone 2, Tuesdays become IWT from week 5). Chart `ruck-long-ruck` is generated by a small Python script (SVG bars like `marathon-long-run`); plan screens `ruck-plan-screens` from `src/plan-ruck-top.jpg` + `plan-ruck-week1.jpg`. The "iRunning Blog Shots" simulator was left in dark mode by the seed flags: the app reads `settings.appearanceMode` from its *container* plist, so `simctl spawn … defaults write interval.irunning` does nothing. Terminate the app, then `xcrun simctl spawn <udid> defaults write "<container>/Library/Preferences/interval.irunning" settings.appearanceMode -string light` (path from `simctl get_app_container … data`, without `.plist`) and relaunch without seed flags. Week 1 opens expanded in the plan detail; use slow short drags (≤160 pt, hold at the end) to position it.
- **October–November 2026 series (written 2026-10-14, 3 posts a week, NYC Marathon 1 Nov as the focus).** Dated 10-16 majors-2027 ballots (updated from the marketing draft; Berlin became the Generali Berlin Marathon, lottery 1 Oct–12 Nov, €215), 10-18 `nyc-marathon-course-guide` (strip figure `nyc-course-strip` from a Python generator, miles not km; fluid pattern from recent editions), 10-20 `how-to-pace-nyc-marathon` (`nyc-pace-profile` chart; split tables computed by an effort model in the scratch script, halves come out equal by design), 10-22 `what-is-a-good-5k-time` (Running Level percentiles; `good-5k-by-age` chart), 10-25 `nyc-marathon-race-week-checklist` (logistics from the 2025 NYRR runner guide PDF, 2026 wave times to confirm), 10-27 `12-3-30-incline-walk` (`PlanCatalog+Incline.swift`; ACE/Wong 2025 study), 10-29 `how-to-watch-nyc-marathon` (2025 broadcast pattern; US clocks go back on race morning, EST), 10-31 `how-to-get-into-nyc-marathon-2027`, 11-05 `winter-running-guide` (reuses `dark-screens.jpg` and `treadmill-plan-screens.jpg`), 11-07 `spring-2027-marathons-when-to-start-training` (plan Mondays = race Sunday − 111 days / − 83 for the half plan). **Still to write:** `berlin`-style results post for NYC on the evening of 1 Nov (facts only). All heroes are Gemini photos generated in the built-in browser pane (user signed in; `canvas.toDataURL()` via javascript_tool, decode with the scratch `decode.py`), prompts in `PROMPTS.md`. Re-check NYC facts against the 2026 runner's guide when NYRR publishes it in the last week of October.
- **November 2026 series W46–W48 (written 2026-10-24, approved list in the marketing repo's `CONTENT_PLAN.md`; Valencia Marathon 6 Dec as the focus).** 11-10 `turkey-trot-5k-first-one` (RunSignup 2025 Thanksgiving report, 1.33M registrants), 11-12 `sub-4-marathon-training-plan` (`PlanCatalog+TimeGoalsLong.swift`, `sub4`: bands mpTempo 5:20–5:32, mpGoal 5:36–5:46, mpFinish 5:38–5:50; chart `sub4-long-run`), 11-14 `valencia-marathon-course-guide` (strip `valencia-course-strip`, km, aid stations from the official 2026 course map), 11-17 `interval-running-apple-watch` (`WatchWorkoutExporter.swift`: WorkoutKit maps warm-up/cool-down, repeat groups, pace → SpeedRangeAlert, HR → bpm range from the user's own zones; always an outdoor run), 11-19 `how-to-pace-valencia-marathon` (`valencia-pace-plan`; split model: +8 s/km km 0–2, +2 to half, goal to km 35, −4 to finish), 11-21 `what-is-a-good-marathon-time` (Running Level marathon tables, Chicago 2026 distribution chart `marathon-finish-distribution`, Boston 2027 standards, cut-off 5:17), 11-24 `how-to-run-longer-without-getting-tired` (`run30` plan, chart `run30-progression`), 11-26 `running-app-without-subscription` (competitor prices as of late Oct 2026: re-check before the date), 11-28 `valencia-marathon-race-week-checklist`. Bar charts come from a small generator; stacked segments are drawn inside one rounded clip path so colour joints stay straight. **Re-check before publishing:** Valencia runner's guide (published race week: bag-drop hours, tram timetable, bib collection by a third party), competitor pricing on 26.11. **Next:** W49 how to watch Valencia (Thu 3.12) and results (Sun 6.12 evening).
- **1.2.4 release post (2026-10-28).** `irunning-1-2-4-countdown-go-back-a-step-live-map`: What's New from ASC (version `64cd3d8e…`, live 2026-10-27) plus a short "in case you missed 1.2.3" section (1.2.3 shipped without a post). Each feature says where to switch it on (paths checked in `SettingsView.swift` / `AudioCuesView.swift`). Figures `v124-countdown-settings`, `v124-return-step`, `v124-live-map` share `v124-pair.css` (two numbered frames); `v124-video-styles` (+ `-mobile`, 2×2). Recipes: the run screen, steps sheet and live map come from the `--debug-run-display classic … --real-map --route-gpx` launch (tap the steps list, long-press the done warm-up; tap the map card's expand icon). The **Apple Watch** section of Audio cues only appears when a paired watch has the app, so "Apple Watch Ultra 3 (49mm)" watchOS 26.4 is now paired with the "iRunning Blog Shots" phone with `iRunningWatch.app` installed. Video-style frames: launch with `--debug-hud-stills` (story still per HUD × light/dark map into `Documents/HUDStills/`, 540×960). In this simulator the first tap after a launch or a scroll is often dropped: screenshot and repeat.
- **1.2.5 release post (written 2026-10-29, not published yet).** Lives in `_drafts/irunning-1-2-5-insights-pace-warm-up-guides.md` with no date, on request: on release day move it to `_posts/<date>-irunning-1-2-5-insights-pace-warm-up-guides.md` and the homepage "New" pill switches to it by itself (it picks the newest dated `releases` post). The `irunning-site-drafts` launch config now also passes `--drafts`, and `scripts/make-blog-thumbs.sh` reads `_drafts/` too. What's New from ASC (version `9913ced1…`, READY_FOR_REVIEW on 2026-10-29); Insights is free for the verdict + rep chart, the rest Premium (`WorkoutInsightsSection.swift`); Pace and Guides are free. Figures `v125-insights`, `v125-pace`, `v125-guides`, `v125-video-ready` reuse `v124-pair.css`; card/OG image `v125-hero` (4 phones). Recipes: `--seed-workout-insights --debug-insights top|bottom` (the seeded workout is called "Insights 6 × 800"; it was renamed to "6 × 800 m" by editing `ZWORKOUT.ZNAME` / `ZRUN.ZWORKOUTNAME` in the app group's `default.store` with the app terminated — relaunch *without* the seed flag or it is re-created), `--seed-share-run --debug-celebration videoCard --debug-scrub 0.55` (then History › Tuesday 400s › Avg pace opens the Pace screen pre-scrubbed; dragging on the chart clears the scrub, so scroll by dragging the map). The old "iRunning Blog Shots" simulator was gone; a new one (iPhone 17 Pro, iOS 26.5, no watch paired) was created. Gotchas on it: the app renders black unless the simulator panel is attached; launch hangs on the splash (CoreLocation XPC) until `simctl privacy … grant location-always` + `simctl location … set`; delete the global `AppleICUForce24HourTime` and reboot for "9:41" instead of "09:41"; the panel's screenshots lag one action behind, so verify with `simctl io … screenshot` after a short sleep (the "dropped taps" were this lag).
- Generated photos (Gemini / Nano Banana) and their exact prompts: `_figures/blog/PROMPTS.md`. Illustration only, never presented as a real user.
- Mobile: wide post tables scroll inside themselves under 480px (`main.css`).

**Backlog of article ideas:** `../irunning-marketing/plans/CONTENT_PLAN.md` and `KEYWORD_RESEARCH.md` in the private marketing repo (priorities, keywords, free/Pro facts). Move a topic to its "published" line there after posting. Keep plans and drafts out of this public repo.

**Content strategy:** benefit-focused articles targeting long-tail keywords (interval running app, couch to 5K Apple Watch, heart rate zones running, run walk method). Every post ends with the automatic App Store CTA. Release posts translate ASO "What's New" into blog form.

---

## Brand / Tone

- **Positioning:** "Run intervals. Get faster." — interval running made simple, on iPhone + Apple Watch
- **Tone:** warm, concrete, coach-like; confident but never hype-y. Numbers over adjectives.
- **Developer / legal entity:** Dzionis Brek (matches App Store + tts-blog legal pages)

---

## Config Values (_config.yml)

```yaml
url: "https://irunning.app"
app_store_url: "https://apps.apple.com/us/app/id6770997508"
ga_measurement_id: "G-XXXXXXXXXX"   # placeholder — replace to enable GA4
permalink: /blog/:year/:month/:title/
```

---

## What This Site Does NOT Have (yet)

- Real App Store review quotes on the homepage (current three are placeholder marketing copy — swap in genuine reviews)
- Dark mode (design system defines tokens; deliberately "daylight first" for now)
- OG image is generated from `scripts`-free manual render — regenerate if hero copy changes
- FAQ section, email capture, search
- `pt=` provider token on App Store links (App Analytics campaign reporting needs it; get it from ASC → Analytics → Sources → generate campaign link)
- Localized pages (app ships 28 locales; site is English-only)

## Scheduled posts

A post dated in the future is built (`future: true`) and reachable by its direct URL, but carries `noindex` and stays out of the blog listing, the homepage preview, `feed.xml` and `sitemap.xml` (all filter on `post.date <= site.time`). `.github/workflows/scheduled-rebuild.yml` asks GitHub Pages to rebuild daily at 09:05 UTC, so the post appears on its date without a push. Posts are dated `09:00:00`, which GitHub Pages reads as UTC, so the rebuild has to run after that; a rebuild at midnight would show the post a day late. Dates without a time are midnight UTC. `feed.xml` is our own copy of the jekyll-feed template (the plugin skips generation when the file exists) — keep the date filter if it's ever replaced. Note: the repo is public, so scheduled post sources are readable on GitHub before their date.
