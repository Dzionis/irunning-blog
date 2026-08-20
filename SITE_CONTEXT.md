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

```
/               — Homepage (hero + phone mockup, interval strip, features, Watch, import/share, reviews, CTA, blog preview)
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

- **GA4 Measurement ID:** NOT SET YET — placeholder `G-XXXXXXXXXX` in `_config.yml` keeps the snippet disabled. Create a GA4 property, paste the real ID, and everything activates.
- Event tracking is data-attribute driven (same system as tts-blog): `data-ga-event`, `data-ga-location`, `data-ga-destination`, handled by delegation in `assets/js/analytics.js`.

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

**8 launch posts** (May–Aug 2026, biweekly): interval builder, Apple Watch, heart rate zones, voice cues, training plans, 2026 running trends, autumn 2026 marathon calendar (Berlin Sep 27 / Chicago Oct 11 / NYC Nov 1 — verified Aug 2026), v1.1.1 release notes.

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

- Real GA4 Measurement ID (snippet auto-disabled until set)
- Real App Store review quotes on the homepage (current three are placeholder marketing copy — swap in genuine reviews)
- Dark mode (design system defines tokens; deliberately "daylight first" for now)
- OG image is generated from `scripts`-free manual render — regenerate if hero copy changes
- FAQ section, email capture, search
- Per-button App Store campaign tokens (`?ct=hero`) — worth adding once GA4 is live
- Localized pages (app ships 28 locales; site is English-only)
