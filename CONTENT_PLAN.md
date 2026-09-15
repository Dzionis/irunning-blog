# Content Plan — iRunning blog

Список тем для статей, собранный 2026-09-15 по коду `irunning-ios` (версия 1.2.2, в ревью) и `ASO_LOCALIZATIONS.md`.
Статьи пишутся на английском. Заголовки ниже — рабочие. Ключевые запросы — гипотезы, частотность не проверялась.

**Уже опубликовано (11):** interval builder · Apple Watch без телефона · HR zones · voice cues · планы walk→5K · тренды 2026 · осенние марафоны · релиз 1.1.1 · Siri & Shortcuts · Action Button · transparent overlays (#4).

**Написано, ждёт выхода 1.2.2 (`published: false`):** #1 Sub-30 5K · #2 Japanese Walking · #3 run video · #5 Zone 2.

Статус: ✅ можно писать сейчас · ⏳ после выхода 1.2.2 в App Store.

Категории (с 2026-09-15 их шесть): `features` — новая функция, `guides` — пошаговая инструкция, `training` — тренировочный гайд вокруг плана или метода, `events`, `news`, `releases`. В таблицах ниже «features» у how-to и планов читать как `guides` / `training`.

---

## Факты, которые нельзя перепутать

- **Бесплатно:** Apple Watch app и забеги с часов, HR-зоны и алерты, pace-таргеты, голосовые подсказки, Live Activity, BLE-пульсометры, импорт из Health/GPX/FIT, «Add to Apple Watch» (WorkoutKit), шеринг картинок и видео, 1 план (From Walk to Run), 3 пресета (Free run, Tabata, Easy run), 2 своих тренировки, история за 7 дней.
- **Pro:** все 41 план, 87 пресетов, безлимит своих тренировок, AI generate, 6 из 8 экранов пробежки, 5 из 7 циферблатов Watch mirror, вся история, экспорт GPX/FIT/Strava/пакетный, iCloud sync (с 1.2.2 — только Pro и выключен по умолчанию).
- **Нет в приложении — не обещать:** адаптация плана по отзыву «Too easy / Too hard» (ответ только сохраняется), auto-pause, пульс с AirPods, достижения/бейджи, экран рекордов, safety/live tracking, учёт кроссовок, complications на часах. «First week free» у планов выключен. Настройка «Always-on display» ничего не делает.
- **Тон:** «coach on a trail walk, not a drill sergeant». Без «crush / grind / no excuses», без давления стриками. Позиционирование: пропустил день — план подстроится вручную за пару тапов, без чувства вины.
- Для медицинских тем (postnatal, после 50, возвращение после травмы) — дисклеймер «Training advice, not medical advice», как в приложении.

---

## 1. Приоритет: первые 10 статей

Порядок выбран по двум признакам: сильный поисковый интерес и функция, которая отличает приложение (или бесплатна).

| # | Рабочий заголовок | Категория | Ключевой запрос | Что из приложения | Статус |
|---|---|---|---|---|---|
| 1 | Sub-30 5K: An 8-Week Plan to Break 30 Minutes | features | sub 30 5k training plan | план Sub-30 5K (8 нед × 4, фиксированные pace-коридоры, алерты SPEED UP / SLOW DOWN) | ⏳ |
| 2 | Japanese Walking: The 3-Minute Interval Walk, Explained | features | japanese walking | план Japanese Walking (8 нед × 4), голосовые подсказки на смену интервала | ⏳ |
| 3 | Turn Your Run Into a Video for Instagram Stories and TikTok | features | running route video / strava video alternative | Share › Video: 5 стилей, 9:16 / 2:3, светлая / тёмная / спутниковая карта, 3D, камера следует за бегуном; бесплатно | ⏳ |
| 4 | Put Your Run Stats on Your Own Photo (17 Transparent Overlays) | features | running stats overlay instagram story | 17 прозрачных PNG-оверлеев, HR route, rep ladder; бесплатно | ✅ |
| 5 | Zone 2 Running: How to Build an Aerobic Base Without Overthinking It | features | zone 2 running | Zone 2 Base Builder (8 нед), HR-зоны, алерты, пресет Zone 2 run, time in zone | ⏳ (план), ✅ (статья без плана) |
| 6 | Moving from Nike Run Club, Strava or Garmin: Bring Your Run History | features | export nike run club runs / import gpx fit iphone | импорт GPX/FIT, Auto-import from Health (90 дней назад), импортированные пробежки получают полную статистику | ✅ |
| 7 | Treadmill Intervals That Don't Feel Like a Hamster Wheel | features | treadmill interval workouts | Indoor-режим без GPS (1.2.2), 8 пресетов Treadmill, Winter Treadmill Plan, 12-3-30 | ⏳ |
| 8 | iRunning 1.2.2: Run Videos, 20 New Plans, Dark Mode | releases | — | What's New 1.2.2 из ASO | ⏳ (день релиза) |
| 9 | Describe Your Run, Get a Workout: AI Workout Builder on iPhone | features | ai running workout generator | AI generate: Apple Intelligence на устройстве, текст или голос; Pro; скрыт без Apple Intelligence | ✅ |
| 10 | Life Happens: Pause, Move or Skip a Training Day Without Starting Over | features | missed training run what to do | Pause plan (1–2 нед / до возобновления), Move a session, Restart week, баннер «Do it today / Skip it» | ✅ |

---

## 2. Как пользоваться функциями (how-to)

| Рабочий заголовок | Суть | Free / Pro | Статус |
|---|---|---|---|
| 8 Run Screen Layouts: Pick the One That Fits Your Workout | Classic, Target hero, Split, Interval card, 4 карточных варианта; locked screen, Slide to unlock, «hold the big number» | 2 free + 6 Pro | ✅ |
| Pace Targets: Run the Right Speed, Not Just Any Speed | коридоры темпа на шаг, IN TARGET / SPEED UP / SLOW DOWN, % времени в таргете, голосовое предупреждение о выходе из коридора | free | ✅ |
| Send Interval Workouts to Apple's Workout App | «Add to Apple Watch» через WorkoutKit, с pace- и HR-алертами. Хороший запрос: custom workout apple watch | free | ✅ |
| Using a Bluetooth Chest Strap With Your iPhone | стандартный BLE-профиль, авто-переподключение, приоритет над часами | free | ✅ |
| Reading Your Run Summary: Training Load, Recovery and Weather | TRIMP, аэробный/анаэробный акцент, часы восстановления, нагрузка за 7 дней, погода Apple Weather | free | ✅ |
| Running Form Metrics Explained: Ground Contact, Vertical Oscillation, Stride | метрики формы (Apple Watch Series 6+ или FIT) + что с ними делать | free | ✅ |
| Your Apple Watch, Your Way: 7 Mirror Faces | зеркалирование телефон ↔ часы, стили экрана, хаптика | 2 free + 5 Pro | ✅ |
| Home Screen Widgets and Live Activity for Runners | виджеты Today's run и Week calendar, Live Activity с кнопками | free | ✅ |
| Schedule Workouts and Get a Quiet Reminder | Schedule по дням недели, уведомление за 10 мин, напоминания плана утром / накануне | free | ✅ |
| Walk or Run? Automatic Detection and Walks as First-Class Workouts | распознавание ходьбы/бега, ходьба сохраняется в Health как ходьба, Share walk | free | ⏳ |
| Upload Runs to Strava (and Export GPX/FIT in Bulk) | Strava OAuth, пакетный экспорт ZIP | Pro | ⏳ (пакетный экспорт) / ✅ (Strava) |
| Dark Mode for Night Runners | короткая статья или абзац в релизе 1.2.2 | free | ⏳ |

---

## 3. Гайды под планы (evergreen SEO)

Схема статьи: польза для читателя → как устроены недели → типичные ошибки → «план в приложении». Состав недель брать из `TRAINING_PLANS_CONTENT.md` и `PlanCatalog*.swift`, аргументы с источниками — из `TRAINING_PLANS_RESEARCH.md`.

**Цель по времени (очень высокий интерес, конкурент — Runna):**
- Sub-60 10K in 10 Weeks ⏳
- Sub-2 Hour Half Marathon: A 12-Week Plan ⏳
- Sub-4 Marathon: 16 Weeks to Break Four Hours ⏳
- The Faster Mile: 6 Weeks of Short, Sharp Speed ⏳

**Ходьба и хайкинг (большая аудитория, растущие тренды):**
- 12-3-30 Incline Walk: Does the Viral Treadmill Workout Work? ⏳
- Rucking for Beginners: Your First 8 Weeks With a Pack ⏳
- You Can Walk a Half Marathon: A 12-Week Plan ⏳
- Brisk Walking for Weight Loss: How Much Is Enough? ✅ (план уже есть)
- Training for the Camino de Santiago: The Last 100K vs the Full Francés ✅ (узкая ниша, сильный интент)
- Trek Ready: Train for a Multi-Day Hike in 10 Weeks ⏳

**Новичкам и тем, кто возвращается:**
- Run-Walk Your First Half Marathon ⏳
- Starting to Run After 50 (First 5K After 50 / Strong Runs at 50+) ⏳
- Postnatal Return to Running: A Gentle 8-Week Path ⏳ — осторожный тон, дисклеймер
- Back After a Break: A 4-Week Return to Running ✅
- Run 30 Minutes Nonstop in 6 Weeks ✅
- The 30-Minute Runner: Fitness When You're Short on Time ⏳

**Дистанции и трейл:**
- Your First 15K or 10-Miler ⏳
- First Trail Race: What Changes Off-Road ✅
- First 50K: Training for Your First Ultra ⏳
- Fitness Racing: 8 × 1 km Between the Stations ⏳ — без торговых марок (решение из спеки плана)

**Здоровье:**
- Easy Runs for a Clear Head: Running for Stress, Not Speed ✅
- A 28-Day Running Habit (Without the Guilt) ⏳ — формулировать без давления стриками

---

## 4. Тренировочная база (статьи по пресетам)

Каждая статья разбирает один тип тренировки и ведёт на готовый пресет. Большинство пресетов в Pro, в статье это стоит упомянуть одной строкой.

- Yasso 800s: The Marathon Predictor Workout
- Fartlek: Unstructured Speed That Actually Works
- Tempo vs Threshold vs Cruise Intervals — What's the Difference?
- Strides: The 20-Second Habit That Makes You Faster (есть в «Easy run + strides» и пресете Strides)
- Hill Repeats for Flat-Land Runners
- Tabata for Runners: 4 Minutes, Done Right (Tabata — бесплатный пресет)
- Negative Splits and Progression Runs
- The 80/20 Rule: Why Most of Your Runs Should Feel Easy
- The 10% Rule Is a Myth — Here's What to Do Instead (из TRAINING_PLANS_RESEARCH.md)
- Recovery Runs, Shake-Outs and Zone 1: When Slow Is the Point

---

## 5. События и новости

- Spring 2027 Half Marathons Worth Training For (events): сегодня 15 сентября, так что это время начинать 12–16-недельные планы
- Winter Running Guide: Dark, Cold, Treadmill (news / features) — связка dark mode + indoor + Winter Treadmill Plan
- Camino Season 2027: When to Walk and How to Prepare (events)
- Best Running Apps for iPhone in 2026: An Honest Comparison (news) — честное сравнение с Runna, Strava, Nike Run Club. Проверять цены и функции конкурентов на дату публикации.

---

## 6. Релизные статьи

- **iRunning 1.2: Make the Run Screen Yours** — догоняющая статья за 1.2.0 и 1.2.1: 8 экранов, настраиваемые подсказки, новые сводки пробежек (погода, форма, «how did it feel»), Siri, 7 циферблатов Watch, «Up next». iCloud описывать нейтрально: в 1.2.2 он стал Pro и выключен по умолчанию.
- **iRunning 1.2.2** — в день выхода (см. §1 #8).

---

## Как использовать

1. Перед статьёй о функции сверять факты с кодом (пути в `SITE_CONTEXT.md` и в самом приложении).
2. ⏳-статьи можно готовить заранее, но пушить только после выхода версии в App Store: на сайте `future: true`, поэтому статья с будущей датой публикуется сразу.
3. После публикации перенести тему в список «Уже опубликовано» вверху.
