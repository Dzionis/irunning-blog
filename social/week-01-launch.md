# Social — неделя 1: запуск (релиз 1.2.2 + Run video)

Источник фактов: `_posts/2026-09-16-irunning-1-2-2-run-videos-plans-dark-mode.md`, `_posts/2026-09-14-run-video-instagram-stories-tiktok.md`.
Копия на английском (аудитория EN). Ссылки: App Store = campaign link с `ct=<канал>` (создать в App Store Connect → App Analytics → Campaigns), блог = `?utm_source=<канал>&utm_medium=social`.

Проверенные факты, которые можно повторять: видеоэкспорт **бесплатный**; 5 стилей (Ink, Frosted glass, Brand block, Side rail, Bleach wash); 9:16 и 2:3; карта light / dark / satellite + 3D; длительность 5–30 с, по умолчанию 12; MP4 без звука, 1080 px, 30 fps; нужен забег с GPS. Планов 41 (было 21). Тёмная тема: Settings › Customise › Appearance. Indoor-режим для дорожки. Пакетный экспорт FIT/GPX и iCloud sync — Premium.

---

## Чек-лист до первого поста (делаете вы)

- [ ] Handle `@irunning.app` (или ближайший свободный) в Instagram, TikTok, Threads, Pinterest, YouTube; FB-страница.
- [ ] Аватар = иконка приложения; био (ниже); ссылка = campaign link.
- [ ] 3 campaign link в ASC: `ig`, `tt`, `reddit`.
- [ ] Записать клипы из списка «Съёмочный лист».

**Био (IG / TikTok / Threads, ≤150 символов):**
> Interval runs, training plans & Apple Watch coaching. Easy days stay easy. 🏃 Free on iPhone ↓

---

## Съёмочный лист (без камеры)

| # | Клип | Как получить | Длина |
|---|---|---|---|
| V1 | Central Park, Brand block, 3D satellite | уже есть: `assets/images/blog/run-video-3d.mp4` | 12 с |
| V2 | Тот же забег, Ink, light map | Share › Video, сид `--seed-share-run` | 12 с |
| V3 | Тот же забег, Frosted glass, dark map | то же | 12 с |
| V4 | Экранная запись редактора: свайп стилей → 3D → Export → «Video ready» | симулятор, `xcrun simctl io booted recordVideo v4.mp4` | 15–20 с |
| V5 | Экранная запись: Settings › Appearance → Dark, затем сводка забега | симулятор | 8 с |
| V6 | Своя реальная пробежка в выходные, любой стиль | телефон | 12 с |

---

## Пн — Reel / TikTok / Shorts #1 (V1)

**Текст поверх (3 плашки по 2 с):**
1. `your run, but make it a movie`
2. `route draws itself · pace counts up`
3. `free in iRunning`

**Подпись:**
> 10.7 km around Central Park, replayed. Distance, pace, time and heart rate count up as the dot moves — you can see every surge.
>
> Share › Video in iRunning. Five styles, 3D maps, free.
>
> #running #runtok #centralpark #applewatch #runningapp #strava

Звук: трендовый из библиотеки площадки, без слов.

---

## Вт — Threads (текст + картинка `video-styles.jpg`)

> Shipped today: your run as a video.
>
> Pick a run → Share → Video. The route draws itself while distance, pace and heart rate tick up. Five looks, light/dark/satellite maps, 3D buildings.
>
> Free, no subscription. Which style would you post?

Второй пост в тот же день (ответом):
> Tip: interval sessions make the best clips. Watching pace jump on every rep is way more fun than a flat line.

---

## Ср — Instagram карусель «iRunning 1.2.2» (+ кросспост FB)

| Слайд | Заголовок | Подтекст | Визуал |
|---|---|---|---|
| 1 | What's new in iRunning 1.2.2 | Swipe → | кадр из V1 |
| 2 | Your run, as a video | Route replay with live stats. Free. | `video-styles.jpg` |
| 3 | 5 looks, 3 maps, 3D | Ink · Frosted glass · Brand block · Side rail · Bleach wash | 3 кадра V1–V3 |
| 4 | 41 training plans | Sub-30 5K → Sub-4 marathon, Japanese walking, rucking, After 50 | `sub30-screens.jpg` |
| 5 | Dark mode | Settings › Customise › Appearance | `dark-screens.jpg` |
| 6 | Indoor runs | No GPS, saved to Health as indoor. Intervals & voice cues as usual. | `treadmill-plan-screens.jpg` |
| 7 | Update now | Try Share › Video on your last run. Tag us 👀 | иконка + handle |

**Подпись:**
> Biggest update since training plans. Run videos (free for everyone), 20 new plans, dark mode and indoor runs. Which one are you trying first?
>
> #running #runningapp #applewatchrunning #trainingplan #couchto5k

---

## Ср — X тред (build in public)

1/ Shipped iRunning 1.2.2 today. The headline: turn any GPS run into a vertical video — route draws itself, stats count up. 🧵
2/ One design rule: the live preview and the exported MP4 come from the same SwiftUI frame. Drag the duration slider, playback updates instantly; export matches the preview frame for frame.
3/ Export renders each frame with ImageRenderer into AVAssetWriter. A 12-second 1080p clip renders in well under a minute on device.
4/ Map backdrop is an MKMapSnapshotter image — including 3D extruded buildings — drawn with a single transform for image, trail and dot so nothing drifts.
5/ It's free. Also in 1.2.2: 20 new training plans (41 total), dark mode, indoor runs. [App Store link]

(Пост 3–4 сверить с кодом перед публикацией, если что-то менялось после 2026-09-14.)

---

## Чт — Reel / TikTok #2 (V4, экранная запись)

**Текст поверх:** `POV: you finally made your run look good` → `swipe for styles` → `3D ✓` → `export` → `done in seconds`

**Подпись:**
> How to turn a run into a video on iPhone:
> History → your run → Share → Video → pick a style → Export.
> Free in iRunning.
>
> #runningtips #iphonetips #runtok #applewatch

---

## Пт — Reel / TikTok #3 (V2 + V3 склейкой, «light or dark?»)

**Текст поверх:** `same run.` → `light or dark?` → `comment 1 or 2`

**Подпись:** `Same 10.7 km, two looks. Team light or team dark? 👇 (Dark mode for the whole app just landed too.)`

Pinterest пачкой (5 пинов 2:3): video-styles, sub30-pace-bands, japanese-walking-hero, treadmill-hero, overlay-stories → ссылка на соответствующие статьи блога.

---

## Сб — своя пробежка (V6) + Stories

Story 1: V6 через кнопку Instagram в «Video ready».
Story 2: опрос `Would you post this? Yes / Needs music`.

---

## Reddit — апдейт в августовском посте (r/BeginnersRunning)

Пост: https://www.reddit.com/r/BeginnersRunning/comments/1vruatr/

Комментарий от автора:
> Update for everyone who gave feedback here: 1.2.2 is out. A few things came straight from this thread — [вставить 1–2 реальных пункта из фидбека]. New: 20 more training plans (incl. run-walk half marathon and a gentle First 5K After 50), dark mode, indoor runs, and a free run-to-video export.
>
> I still owe lifetime unlocks to the people who replied — sending codes by DM today. Thanks again.

⚠️ Перед этим сгенерировать 10 offer codes для `59.irunning.lifetime` (в памяти отмечено как не сделанное) и разослать их тем, кто оставил фидбек.

---

## Reddit — шаблоны ответов (использовать, только когда вопрос реально об этом)

**«Как сделать видео маршрута как в Relive / Strava?»**
> If you're on iPhone, a few apps export route replays now. Relive is the classic one. iRunning (disclosure: I made it) does it free — Share › Video on any GPS run, 9:16 for Stories, stats count up as you go. For a still image, Strava's share cards are fine too.

**«Как бегать интервалы на Apple Watch?»** → ссылка на статью `how-to-build-interval-workouts-on-iphone`, три способа, приложение третьим пунктом с disclosure.

Правило: disclosure всегда, ссылка на статью чаще, чем на App Store, 10 полезных ответов без упоминания на 1 с упоминанием.
