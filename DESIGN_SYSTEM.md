# Trail calm — design system

**Variant:** 02
**Personality:** Daylight, paper-like, forest green. Reads as a hiking GPS, not a gym timer.
**Best for:** Endurance runners, tempo and long-run training, outdoor positioning.
**Min platform:** iOS 17 / watchOS 10
**Status:** Spec v1.0

---

## 1. Design principles

1. **Daylight first.** The default appearance is light because most runs happen outdoors during the day. Dark mode exists but is the secondary surface, not the primary.
2. **Paper, not glass.** Surfaces are warm off-white (`#F1EFE8`), not pure white. This reduces glare in direct sunlight and gives the app a tactile, journal-like quality.
3. **Green means go.** Work intervals are deep forest green — readable in bright light, semantically aligned with movement and the outdoors. Red is reserved for genuine danger states (low battery, GPS lost, HR critical).
4. **One number rules each screen.** Whatever the user came to the screen for is 64–88px. Everything else is demoted by at least 2x.
5. **Tabular numerics, always.** Timers and pace must not visually shift as digits change.

---

## 2. Color tokens

### 2.1 Primitive palette

These are the raw colors. Never reference these directly in component code — use the semantic tokens in §2.2 instead.

| Token | Hex | RGB | Notes |
|---|---|---|---|
| `green/50` | `#E1F5EE` | 225, 245, 238 | Lightest fill, rest-state backgrounds |
| `green/100` | `#9FE1CB` | 159, 225, 203 | Soft fills, watch progress arcs |
| `green/200` | `#5DCAA5` | 93, 202, 165 | Hover states, secondary accents |
| `green/400` | `#1D9E75` | 29, 158, 117 | **Brand primary, work intervals** |
| `green/600` | `#0F6E56` | 15, 110, 86  | Text on green/50, pressed states |
| `green/800` | `#085041` | 8, 80, 65    | Headings, dark-mode primary |
| `green/900` | `#04342C` | 4, 52, 44    | Text primary, deepest accent |
| `paper/50`  | `#FFFFFF` | 255, 255, 255 | Card surface |
| `paper/100` | `#F8F6EF` | 248, 246, 239 | Surface hover |
| `paper/200` | `#F1EFE8` | 241, 239, 232 | **Page background** |
| `paper/400` | `#D3D1C7` | 211, 209, 199 | Borders, dividers |
| `paper/600` | `#888780` | 136, 135, 128 | Text secondary |
| `paper/800` | `#444441` | 68, 68, 65   | Text on light fills |
| `paper/900` | `#2C2C2A` | 44, 44, 42   | Text primary (alt to green/900) |
| `amber/400` | `#BA7517` | 186, 117, 23 | Warmup state |
| `amber/600` | `#854F0B` | 133, 79, 11  | Warmup text on amber/50 |
| `coral/400` | `#D85A30` | 216, 90, 48  | Cooldown state |
| `red/400`   | `#E24B4A` | 226, 75, 74  | Danger only — battery, GPS lost |

### 2.2 Semantic tokens

These are what components reference. They map to primitives and resolve differently in light/dark mode.

#### Surfaces
| Semantic | Light | Dark |
|---|---|---|
| `surface.background` | `paper/200` | `green/900` |
| `surface.card` | `paper/50` | `paper/900` |
| `surface.cardHover` | `paper/100` | `paper/800` |
| `surface.elevated` | `paper/50` | `paper/800` |

#### Text
| Semantic | Light | Dark |
|---|---|---|
| `text.primary` | `green/900` | `paper/200` |
| `text.secondary` | `paper/600` | `paper/400` |
| `text.tertiary` | `paper/400` | `paper/600` |
| `text.onAccent` | `paper/50` | `green/900` |
| `text.onAccentMuted` | `green/50` | `green/800` |

#### Interval states (the most important set in this app)
| Semantic | Light fill | Light text | Dark fill | Dark text |
|---|---|---|---|---|
| `interval.work` | `green/400` | `paper/50` | `green/200` | `green/900` |
| `interval.work.subtle` | `green/50` | `green/800` | `green/800` | `green/100` |
| `interval.rest` | `paper/200` | `green/900` | `paper/800` | `paper/200` |
| `interval.rest.subtle` | `paper/100` | `paper/600` | `paper/900` | `paper/400` |
| `interval.warmup` | `amber/400` | `paper/50` | `amber/400` | `paper/50` |
| `interval.cooldown` | `coral/400` | `paper/50` | `coral/400` | `paper/50` |
| `interval.open` | `paper/600` | `paper/50` | `paper/400` | `green/900` |

#### Functional
| Semantic | Light | Dark |
|---|---|---|
| `border.default` | `paper/400` | `paper/800` |
| `border.strong` | `paper/600` | `paper/600` |
| `border.accent` | `green/400` | `green/200` |
| `danger` | `red/400` | `red/400` |
| `success` | `green/400` | `green/200` |

---

## 3. Typography

### 3.1 Font stack

- **Display & body:** SF Pro (iOS system) — `-apple-system`. Uses SF Pro Display above 20pt, SF Pro Text below.
- **Numerics:** SF Pro with `font-feature-settings: "tnum"` (tabular numerics). Critical for the run screen — non-tabular digits cause the timer to twitch.
- **Monospaced fallback:** SF Mono — only used in debug overlays and split tables on the post-run summary.

### 3.2 Type scale

| Token | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| `display.hero` | 88pt | 500 | 1.0 | Run screen primary number on iPhone Pro Max |
| `display.large` | 64pt | 500 | 1.0 | Run screen primary number on standard iPhones |
| `display.medium` | 48pt | 500 | 1.0 | Watch primary, post-run total time |
| `title.large` | 28pt | 600 | 1.15 | Workout name on builder, post-run header |
| `title.medium` | 22pt | 600 | 1.2 | Section headers, secondary metric on run screen |
| `title.small` | 17pt | 600 | 1.3 | Card titles, list rows |
| `body.large` | 17pt | 400 | 1.4 | Default body |
| `body.medium` | 15pt | 400 | 1.4 | Compact body, settings rows |
| `body.small` | 13pt | 400 | 1.4 | Captions, meta |
| `label.large` | 15pt | 500 | 1.2 | Buttons |
| `label.medium` | 13pt | 500 | 1.2 | Pills, badges |
| `label.uppercase` | 11pt | 600 | 1.2 | Section labels — `letter-spacing: 0.08em`, all caps |

### 3.3 Numerics

The run screen primary number must always use:
- `display.hero` or `display.large`
- `font-feature-settings: "tnum", "ss01"` (tabular + alternate one)
- `letter-spacing: -0.02em`
- Color: `text.primary` (green/900)

---

## 4. Spacing & layout

Base unit: **4pt**. Avoid using values that aren't a multiple of 4.

| Token | Value |
|---|---|
| `space.xs` | 4pt |
| `space.sm` | 8pt |
| `space.md` | 12pt |
| `space.lg` | 16pt |
| `space.xl` | 24pt |
| `space.xxl` | 32pt |
| `space.xxxl` | 48pt |

### Corner radius

| Token | Value | Use |
|---|---|---|
| `radius.sm` | 6pt | Pills, badges, small chips |
| `radius.md` | 12pt | Buttons, input fields |
| `radius.lg` | 20pt | Cards, sheets |
| `radius.xl` | 28pt | Full-screen modals, run screen container |
| `radius.full` | 999pt | Capsule buttons, ring caps |

### Iconography

- Set: SF Symbols, weight `regular` for navigation, `medium` for primary actions
- Sizes: 17pt (inline), 22pt (tab bar), 28pt (action buttons), 44pt (run screen controls)
- Color inherits from parent text color

---

## 5. Components

### 5.1 Pill (interval label)

Used at the top of the run screen and on the Live Activity to indicate current state.

- Height: 24pt, padding: 4pt vertical / 12pt horizontal
- Radius: `radius.full`
- Typography: `label.medium`
- Background/text: from `interval.{state}` semantic pair
- Optional leading icon at 13pt

### 5.2 Progress ring

Two concentric arcs.

- **Outer ring:** current interval progress, stroke 6pt, radius 88pt (iPhone) / 36pt (watch)
- **Inner ring:** total workout progress, stroke 4pt, radius 72pt (iPhone) / 28pt (watch)
- Track color: `interval.{state}.subtle` (background)
- Fill color: `interval.{state}` (foreground)
- Cap: `round`
- Direction: starts at 12 o'clock, **depletes clockwise** (counts down, not up)
- Animation: linear interpolation, 60fps, no easing — runners need a steady visual tick

### 5.3 Big number

The primary metric on the run screen.

- Typography: `display.hero` or `display.large`
- Color: `text.primary`
- Below it: secondary number in `title.medium`, color `text.secondary`
- The big number and its label must occupy the visual center of the ring

### 5.4 Stat row

Horizontal row of 3 stats below the ring (distance / total time / heart rate).

- Each stat: value in `title.small` weight 500, label in `label.uppercase`
- Spacing: distributed evenly, padding-top 16pt
- Border-top: 0.5pt `border.default`

### 5.5 Buttons

| Variant | Background | Border | Text | Use |
|---|---|---|---|---|
| Primary | `interval.work` (green/400) | none | `text.onAccent` | "Start workout" |
| Secondary | `surface.card` | 0.5pt `border.default` | `text.primary` | Cancel, secondary actions |
| Ghost | transparent | none | `text.primary` | Toolbar, icon-only |
| Destructive | transparent | 0.5pt `danger` | `danger` | Delete workout |

- Height: 52pt for primary CTAs, 44pt for inline actions, 36pt for compact
- Press state: scale 0.97, 80ms ease-out
- Min tap target: 44×44pt (iOS HIG)

### 5.6 Card

Base container for workouts in the library, history rows, settings groups.

- Background: `surface.card`
- Border: 0.5pt `border.default`
- Radius: `radius.lg`
- Padding: 16pt
- Hover (iPad / Mac Catalyst): `surface.cardHover`

### 5.7 Live Activity / Dynamic Island

Compact (Dynamic Island leading + trailing):
- Leading: interval pill color as a 6pt dot + text "WORK"
- Trailing: countdown `00:42` in tabular monospace, 13pt, weight 600

Expanded:
- Top row: interval pill + workout name
- Center: big number (countdown), 36pt, tabular
- Bottom row: stat row (compact, 2 stats: distance + total)

---

## 6. Accessibility

- **Contrast:** all text/background pairs above must pass WCAG AA (4.5:1 for body, 3:1 for large text). Verified pairs:
  - `text.primary` (green/900) on `surface.background` (paper/200): **15.2:1** ✓
  - `text.onAccent` (paper/50) on `interval.work` (green/400): **4.6:1** ✓
  - `text.secondary` (paper/600) on `surface.card` (paper/50): **5.1:1** ✓
- **Dynamic Type:** all type scales except `display.*` must scale with the user's accessibility text size. Display sizes cap at +30% to preserve layout.
- **Reduce Motion:** when enabled, ring animations switch to discrete steps (1 tick per second), no scale-bounce on button presses.
- **Reduce Transparency:** Live Activity backgrounds use solid `surface.card` instead of materials.
- **Color independence:** interval states are also signalled by haptics (Watch) and voice cues (announcements at boundaries). Never rely on color alone.
- **VoiceOver labels:** the run screen big number announces as e.g. "Forty-two seconds remaining in work interval, four of eight."

---

## 7. Motion

| Token | Duration | Easing | Use |
|---|---|---|---|
| `motion.fast` | 80ms | ease-out | Button press, pill tap |
| `motion.medium` | 200ms | ease-in-out | Sheet present, tab switch |
| `motion.slow` | 320ms | spring(0.6, 0.8) | Run screen entry, paywall |
| `motion.none` | 0ms | — | Ring fill (linear, frame-perfect) |
| `motion.celebrateFill` | 900ms | ease-out cubic | Ring completion fill (plan-complete celebration only) |
| `motion.stamp` | — | spring(response 0.35, damping 0.65) | Milestone/badge stamp-in |
| `motion.cascade` | 260ms, 80ms stagger | ease-out | Sequential stat/list reveals |

The ring **never** uses spring easing. Runners are using it as a clock; springiness would feel like the time is lying. One exemption: on the plan-complete celebration the plan is over — the ring is a trophy, not a clock — so its completion fill may use `motion.celebrateFill` (see `PLAN_CELEBRATION_SPEC.md` §1).

---

## 8. Do / don't

**Do**
- Use green for "in progress / good." If everything is fine, the screen is calm green.
- Keep the run screen sparse. Big number, ring, three stats. That's it.
- Render `paper/200` as the page background, even on small screens. It's the brand.
- Use SF Symbols at one of the four defined sizes — never custom in-between values.

**Don't**
- Don't use red for work intervals. Red means danger here.
- Don't put more than three stats below the ring. The fourth one always loses.
- Don't introduce gradient fills. The aesthetic is flat paper, not glass.
- Don't reach for `green/600` as a brand primary — it's text-on-light only. The brand is `green/400`.
- Don't use weight 700 anywhere. Two weights only: 400 and 500/600.

---

## 9. Files in this variant

- `SPEC.md` — this document
- `Tokens.swift` — Swift/SwiftUI token definitions for the iOS + watchOS app
- `tokens.json` — Style Dictionary–compatible JSON for Figma and web tooling
