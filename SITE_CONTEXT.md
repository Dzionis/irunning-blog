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
- Radii: 6 / 12 / 20 / 28 / 999 px (sm/md/lg/xl/full)
- Stats/numbers use tabular numerics (`font-variant-numeric: tabular-nums`)
- Category tag colors mirror the app's interval states:
  - `features` → green (work), `events` → amber (warmup), `releases` → coral (cooldown), `news` → neutral paper (rest)
- Hero, Watch section, and the "From First Step to Finish Line" gallery use **real simulator screenshots** in CSS device frames (`.phone`/`.phone-screen-shot`, `.watch-body`/`.watch-screen`, `.shot-frame`)

## Regenerating app screenshots

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
/               — Homepage (hero + real run screenshot with soft shadow, "Your session" proportional-bar strip, features, Watch, screens gallery, import/share, reviews, CTA, blog preview)
/blog/          — Blog listing (all posts)
/blog/:year/:month/:title/  — Individual posts
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
| `_includes/header.html` | Site header (icon + iRunning, nav: Blog, Get App) |
| `_includes/footer.html` | Dark green footer (brand, nav links, copyright) |
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
| `blog_post_click` | Blog cards (homepage preview + listing) |
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

**Post figures** live in `assets/images/blog/` (PNG @2x, 1440px wide + a 800px `-mobile` variant served via `<picture>` under 560px, because text in a 720px figure is unreadable at phone width). Styled by `.post-figure` in `main.css`. Sources are HTML pages in `_figures/blog/` (Jekyll ignores the folder); re-render one with `_figures/blog/render.sh <name>` (headless Chrome, height read from `.canvas`). The app screens inside them (`announce.png`, `run-classic.png`, `run-locked.png`) were captured without any tapping via the app's DEBUG launch flag: `xcrun simctl launch <udid> interval.irunning --debug-run-display announce` (also `classic --target hr`, `classicLock --locked`, `pickerRun`, `pickerLocked`; see `RunDisplayDebugScreen.swift`). Launch iRunning right after another app and iOS adds a "◂ Settings" back-link to the status bar, so terminate other apps first.

**Waiting posts (`published: false`).** Four posts depend on iRunning 1.2.2 and are hidden from the build until it's live on the App Store (still IN_REVIEW on 2026-09-15): `zone-2-running-aerobic-base` (dated 09-06), `japanese-walking-interval-walk` (09-09), `sub-30-5k-training-plan` (09-12), `run-video-instagram-stories-tiktok` (09-14). Dates were deliberately set in the past (2026-09-15 decision) so the blog reads as a steady cadence; to publish just delete `published: false` and rebuild. The three 1.2.0-era how-to posts are live and dated 08-27 / 09-01 / 09-03 (1.2.0 reached the store ~08-30, 1.2.1 ~09-10). Preview them locally with the `irunning-site-drafts` launch config (`jekyll serve --unpublished`, port 4001). Never `post_url`-link a published post to a hidden one: the build fails.

**More figure recipes (Sep 2026).**
- Photo-heavy composites opt into JPEG with `<html data-format="jpg">`; `render.sh` converts them. Screenshots and photo backgrounds they use live in `_figures/blog/src/`.
- Real app screens beyond the run display need taps. Seed data first: `xcrun simctl launch <udid> interval.irunning --seed-share-run --seed-share-walk --seed-home-block active --debug-brand-tiles` ("Tuesday 400s", Berlin loop, full HR; brand tiles force the Instagram/TikTok buttons on a simulator).
- Transparent overlay PNGs (1080×1920, alpha): in the share picker tap the nav-bar **Share** on an overlay, then collect `tmp/*-story.png` from `xcrun simctl get_app_container <udid> interval.irunning data`.
- Run videos: Share › Video › Export video writes `tmp/irun-…-video-story.mp4` in the same container. The seed run's route is synthetic and cuts through buildings, so the video figures use an imported real route instead: `_figures/blog/gpx/make-central-park-loop.py` builds a GPX along Central Park's drives (Overpass geometry + drive-only Dijkstra, timed with a pace plan and heart rate); drop it into the simulator's Files storage (`…/Shared/AppGroup/<group.com.apple.FileProvider.LocalStorage>/File Provider Storage/`) and import it via History › import › "GPX or FIT file" › Browse › On My iPhone. Run name "Central Park Loop", 10.7 km, 56:00. Frames were pulled with an AVFoundation Swift script, and the web copy re-encoded to 540×960 H.264 at 1.4 Mbps (~2.1 MB for 12 s) because Homebrew ffmpeg is broken on this machine. Don't go lower: 800 kbps already softened the satellite map and small caps noticeably. Embedded as a plain `<video autoplay muted loop playsinline>` in `.post-figure.video-figure` (40px vertical margins, 320px wide, rounded corners). A stories-style phone mock was tried on 2026-09-15 and removed on request: keep it plain. `.post-figure video` must keep `height: auto` — the `height` attribute otherwise letterboxes the 320px-wide video to 960px tall. The `src` carries a `?v=YYYYMMDD` query: bump it whenever the MP4 is replaced at the same path, or browsers keep a cached (possibly truncated) copy and report a format error.
- Generated photos (Gemini / Nano Banana) and their exact prompts: `_figures/blog/PROMPTS.md`. Illustration only, never presented as a real user.
- Mobile: wide post tables scroll inside themselves under 480px (`main.css`).

**Backlog of article ideas:** `CONTENT_PLAN.md` (priorities, keywords, free/Pro facts, what's unreleased). Move a topic to its "published" line after posting.

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
