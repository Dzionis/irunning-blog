# Keyword research — сентябрь 2026

Исследование частотности, популярных запросов и растущих трендов вокруг бега/ходьбы, сделано 2026-09-16.
На его основе — 30 предложений статей (§4). Дополняет `CONTENT_PLAN.md`: там полный бэклог по функциям приложения, здесь — что реально ищут.

## 1. Методика и что означают цифры

| Источник | Что даёт | Ограничение |
|---|---|---|
| **Google Trends**, US, последние 12 мес, 4 сравнения по 5 запросов | относительный интерес (0–100 внутри сравнения), сезонность, «rising» запросы | нет абсолютных объёмов; сравнения сшиты через общий запрос `couch to 5k`, поэтому кросс-таблица ниже — приближение |
| **Google Autocomplete**, ~115 сидов (`scratchpad/kw/suggest*.json`) | какие уточнения реально набирают (модификаторы: `calculator`, `in km`, `apple watch`, `without …`) | показывает спрос и интент, не объём |
| **Отчёты**: Strava Year in Sport 2025, Garmin 2026 Running Report, PureGym Fitness Report 2025/26, risingtrends.co, SGI Europe «Running: state of play 2026» | рост год к году, абсолютные объёмы для нескольких запросов | у PureGym проценты роста поисков, база не раскрыта |

Всё, что помечено «≈», — оценка по графику Trends, а не число из API.

## 2. Шкала интереса (Google Trends, US, 12 мес)

Нормировано так, что `couch to 5k` = 100.

| Запрос | Индекс | Сезонность / заметки |
|---|---|---|
| `12 3 30` | ≈ 420 | пик июнь–июль 2026; самый большой из всего измеренного |
| `marathon training plan` | ≈ 180 | пики окт 2025 и янв 2026 (осенние старты → весенние планы) |
| `rucking` | ≈ 170 | ровный интерес весь год |
| `japanese walking` | ≈ 125 | всплеск июнь 2026 (TV-эффект: rising «al roker japanese walking workout» — breakout) |
| `couch to 5k` | 100 | пики январь и июнь; NHS-приложение: 790 000 загрузок в 2024 |
| `half marathon training plan` | ≈ 85 | пики окт и янв; у Garmin Coach полумарафон — самая популярная цель |
| `zone 2 running` | ≈ 60 | общий `zone 2` заметно больше: ≈ 0,8× от `hyrox`, пик март–июнь |
| `5k training plan` | ≈ 30 | ровно |
| `10k training plan` | ≈ 15 | ровно; интент есть в автодополнении (`8 weeks`, `3 days a week`) |

Отдельные сравнения:

- **Типы тренировок:** `hyrox` ≈ 22 (и резкий рост в сентябре 2026), `zone 2` ≈ 18, `interval running` / `tempo run` / `run walk method` ≈ 1 каждый. Люди ищут не названия методов, а результат («how to run longer», «sub 30 5k»).
- **Приложения:** `strava` ≈ 68 (пик январь = 100), `running app` ≈ 32 (пик март–июнь ≈ 55, спад к сентябрю), `runna` ≈ 10, `nike run club` ≈ 5, `running app territory` ≈ 0 — слишком ново для Trends, но уже в 4 кластерах автодополнения.
- **Rising (12 мес):** `tai chi walking`, `al roker japanese walking workout` (breakout), `hyrox` (рост в конце периода).

## 3. Что говорят отчёты

- **PureGym 2025/26:** Japanese walking +2 900 %, walking yoga +2 414 %, plank hover +967 %, **10-20-30 method +467 %**, **Hyrox +171 %**, 5K training plans +50 %, ultra-marathon plans +50 %.
- **Strava YIS 2025:** бег — спорт №1, ходьба №2; клубов ×4 (1 млн), беговых клубов 3,5×, хайкинг-клубов 5,8×; Gen Z на 75 % чаще мотивированы стартом; 46 % готовы пользоваться AI-тренером; Apple Watch — часы №1.
- **Garmin 2026:** беговая дорожка +12,6 % против улицы +3,2 %; средняя пробежка 7,76 км; +23 % «бег + силовая»; полумарафон — самая популярная цель Garmin Coach; 30–39 — самая быстрорастущая группа.
- **risingtrends.co:** `run club` 27 100/мес (+50 %), `hyrox workout` 49 500/мес (+22 %), `obstacle racing` 18 100/мес (+174 %).
- **SGI Europe 2026:** 6 % британцев хотят начать бегать в 2026 (≈ 4,6 млн); 18 % хотят бегать больше (13 % год назад); 27 % женщин и 20 % мужчин считают беговые клубы «только для быстрых»; 17,2 млн трейлраннеров в США (+6,6 %); женщины 35–50 — самая быстрорастущая группа в трейле; 5K — 54 % событий и ⅔ регистраций в США.
- **Territory-apps:** INTVL 2,4 млн пользователей, KYRO, Motera; автодополнение: `running app claim territory`, `running app that claims territory`, `running app with territory`, `interval running app territory`.

## 4. Тридцать статей

Столбцы: целевой запрос (главный + уточнения из автодополнения) · доказательство · что из приложения · категория · статус (✅ можно сейчас, ⏳ после 1.2.2) · приоритет (★★★ первыми).

### 4.1 Можно писать сейчас

| # | Рабочий заголовок | Целевые запросы | Доказательство | Что из приложения | Кат. | Статус | Прио |
|---|---|---|---|---|---|---|---|
| 1 | What's a Good 5K Time? (and 10K, Half — by Age and Sex) — серия из 3 страниц | `what is a good 5k time` (+ by age / for a woman / for a beginner), то же для 10k и half | три кластера автодополнения по 10 вариантов каждый; вечнозелёный запрос | таблицы времени → планы Faster 5K ✅, Sub-30 5K / Sub-60 10K / Sub-2h ⏳ | training | ✅ | ★★★ |
| 2 | Why Is My Heart Rate So High When I Run Slowly? | `why is my heart rate so high when running slow` (+ but I feel fine / compared to others) | 10 вариантов в автодополнении; связка с zone 2 (≈ 0,8× hyrox) | HR-зоны, time in zone, алерты, Zone 2 Base Builder ⏳ | training | ✅ | ★★★ |
| 3 | How to Run Longer Without Getting Tired | `how to run longer without getting tired`, `how to breathe while running`, `why does running get easier` | три больших кластера новичков; UK: 6 % хотят начать бегать | pace-таргеты (SLOW DOWN), голосовые подсказки, Run 30 Minutes Nonstop ✅ | training | ✅ | ★★★ |
| 4 | How to Start Running From Zero (Out of Shape, Overweight, or Again After Years) | `how to start running from zero` / `when overweight` / `again`, `running for beginners plan` | кластер `how to start running` — 10 вариантов; `running plan for obese beginners pdf` | Start Walking, From Walk to Run (бесплатно), Return to Running ✅ | guides | ✅ | ★★★ |
| 5 | Couch to 5K Week by Week: What Each Week Does, and Why People Quit in Week 5 | `couch to 5k week 5` / `week 4`, `couch to 5k app free`, `couch to 5k plan` | индекс 100, пики январь и июнь; NHS-приложение 790 000 загрузок/год | план 0→5K (бесплатно), баннер «Do it today / Skip it», Restart week | training | ✅ | ★★★ |
| 6 | Running App Without a Subscription (or an Account): What's Free in iRunning vs Runna, Strava and NRC | `free running apps like runna`, `running app without subscription` / `without account` / `without login`, `free running apps with training plans` | два кластера `running app without…` и `free running app`; `runna` ≈ 2× `nike run club` в Trends | в приложении нет регистрации; бесплатный слой: Watch, HR-зоны, импорт, шеринг, план 0→5K | news | ✅ | ★★★ |
| 7 | Strava Alternatives for iPhone in 2026 (and How to Move Your History) | `strava alternative free` / `for walking` / `for routes`, `strava alternatives` | `strava` ≈ 68 — крупнейший бренд-запрос; кластер альтернатив 10 вариантов | импорт GPX/FIT/Health, экспорт в Strava (Pro), видео маршрута | news | ✅ | ★★★ |
| 8 | Interval Running on Apple Watch: Three Ways (Workout App, WorkoutKit, iRunning) | `apple watch running intervals`, `how to do interval running on apple watch`, `running interval app for apple watch` | три кластера; Apple Watch — часы №1 на Strava | «Add to Apple Watch» (WorkoutKit, бесплатно), watch-app, 7 циферблатов | guides | ✅ | ★★★ |
| 9 | Zone 2 on Apple Watch — and Without a Heart Rate Monitor | `how to run zone 2 with apple watch` / `without heart rate monitor` / `on treadmill`, `zone 2 heart rate` | кластер `how to run zone 2` — 10 вариантов; пик март–июнь | HR-зоны + алерты, голосовые подсказки, BLE-ремень, Indoor ⏳ | guides | ✅ | ★★ |
| 10 | Easy Run Pace: How Slow Is Slow Enough (Chart + Calculator) | `easy run pace calculator` / `based on 5k time` / `chart`, `running pace calculator`, `running pace chart km` | `calculator` встречается в 11 кластерах автодополнения | pace-таргеты, «% времени в таргете»; см. §5 про калькуляторы | training | ✅ | ★★ |
| 11 | Garmin vs Apple Watch for Running in 2026: Accuracy, Battery, and Whether It Matters | `garmin vs apple watch for running` / `accuracy` / `heart rate accuracy` | кластер 10 вариантов; `garmin` — крупный бренд-запрос | приложение работает с обоими: Watch нативно, Garmin через Health/FIT | news | ✅ | ★★ |
| 12 | The 10-20-30 Workout: 12 Minutes of Speed That Fits Any Week | `10-20-30 running`, `10 20 30 method` | PureGym: +467 % за год | собрать в билдере или AI-билдером («5 × (30s easy, 20s moderate, 10s hard)»); пресета нет — кандидат на добавление | training | ✅ | ★★ |
| 13 | VO₂ Max Intervals: The Norwegian 4×4 for Runners | `vo2 max running workouts` (1-я подсказка кластера), `norwegian 4x4 running` / `for beginners` | два кластера; тема из подкастов о долголетии | пресеты VO₂ max (5 × 3:00) и VO₂ short (8 × 90s) — Pro; 4×4 собирается в билдере с HR-таргетом | training | ✅ | ★★ |
| 14 | Walking vs Running for Weight Loss: What the Numbers Say | `running vs walking for weight loss`, `walking for weight loss plan` / `app`, `can you lose weight walking 10000 steps a day` | четыре кластера про вес; ходьба — спорт №2 на Strava | Brisk Walking for Weight Loss, Weight Loss Kickstart ✅; 12-3-30 ⏳. Аккуратный тон, без обещаний | training | ✅ | ★★ |
| 15 | Should You Run Every Day? What 28 Days Actually Look Like | `running every day for a month results`, `can i run every day as a beginner`, `should i run every day or take breaks` | два кластера по 10 вариантов | 28-Day Streak ⏳ (писать без давления стриками), Maintenance ✅ | training | ✅ (ссылка на план позже) | ★★ |
| 16 | Trail Running for Beginners: What Changes Off-Road | `trail running for beginners`, `how do you train for trail running`, `trail running trends 2026` | 17,2 млн трейлраннеров в США (+6,6 %); женщины 35–50 — самая быстрорастущая группа; ITRA-гонок +131 % | First Trail Race, Trail: Hills & Vert ✅ | training | ✅ | ★★ |
| 17 | Half Marathon Training Plan: 12 Weeks, in Kilometres | `half marathon training plan 12 weeks` / `in km` / `for beginners` / `free` | индекс ≈ 85, пики окт и янв; полумарафон — цель №1 в Garmin Coach | план Half Marathon (12 нед × 4, в км) ✅ — флагман Pro | training | ✅ | ★★★ |
| 18 | Your First Marathon: A 16-Week Plan for Beginners | `marathon training plan for beginners` / `16 weeks` / `km` / `free`, `first marathon time` | индекс ≈ 180 — самый частый из «план»-запросов; пики окт и янв → публиковать в декабре | план Marathon ✅ (id `marathon`), позже Sub-4 ⏳ | training | ✅ | ★★★ |
| 19 | Territory-Claiming Running Apps, Explained (and What Happens After the Novelty) | `running app claim territory`, `running app that claims territory`, `running app with territory` | breakout в 4 кластерах автодополнения; INTVL 2,4 млн пользователей; в Trends ещё ≈ 0 → ранний вход | прямого аналога нет; честный обзор, мостик к видео маршрута и шерингу | news | ✅ | ★ |
| 20 | Run Clubs Aren't Just for Fast People: How to Join One and Keep Up | `run club near me`, `running app with friends`, `how to start a run club` | `run club` 27 100/мес (+50 %); клубы ×4 на Strava, UK +421 %; 27 % женщин считают клубы «для элиты» | pace-таргеты «держать темп группы», run-walk, share-карточки | guides | ✅ | ★ |

### 4.2 После выхода 1.2.2

| # | Рабочий заголовок | Целевые запросы | Доказательство | Что из приложения | Кат. | Статус | Прио |
|---|---|---|---|---|---|---|---|
| 21 | 12-3-30 Incline Walk: Does the Viral Treadmill Workout Work? | `12 3 30 workout` / `in km` / `calories burned` / `before and after`, `what is 12-3-30` | индекс ≈ 420 — максимум всего исследования; пик июнь–июль | план 12-3-30 Incline Walk (6 нед × 3), Indoor-режим | training | ⏳ | ★★★ |
| 22 | Sub-4 Marathon: 16 Weeks to Break Four Hours | `sub 4 marathon training plan`, `marathon training plan 16 weeks`, `easy run pace for 4 hour marathon` | см. #18; `easy run pace for 4 hour marathon` в автодополнении | Sub-4 Marathon (16 нед × 4) | training | ⏳ | ★★★ |
| 23 | Sub-2 Hour Half Marathon: A 12-Week Plan | `how to run a half marathon in under 2 hours`, `half marathon in 2 hours pace`, `sub 2 half marathon plan` | кластер `how to run a half marathon` — 3 из 10 подсказок про время | Sub-2h Half Marathon (12 нед × 4) | training | ⏳ | ★★★ |
| 24 | Sub-60 10K in 10 Weeks (and How to Run Your First 10K) | `how to run a 10k in under an hour`, `10k training plan 8 weeks` / `3 days a week` / `beginner` | индекс ≈ 15, но интент точный; First 10K ✅ закрывает «first» | Sub-60 10K (10 нед × 4), First 10K, 5K→10K | training | ⏳ | ★★ |
| 25 | Rucking for Beginners: Your First 8 Weeks With a Pack | `rucking for beginners`, `rucking weight` / `backpack` / `calorie calculator`, `what is rucking` | индекс ≈ 170 — стабильно выше `couch to 5k` | Rucking: First 8 Weeks (8 нед × 3), Trek Ready | training | ⏳ | ★★★ |
| 26 | Run-Walk Your Way to a Half Marathon (Jeffing, Explained) | `run walk method for half marathon`, `jeffing calculator` / `app`, `what is jeffing` | два кластера (`run walk method`, `jeffing`) по 10 вариантов; в Trends US ≈ 1 — UK-термин | Run-Walk Half Marathon (14 нед × 3), билдер run/walk-интервалов, голосовые подсказки | training | ⏳ | ★★ |
| 27 | Fitness Racing: Training for the 8 × 1 km Between Stations | `hyrox running plan`, `running plan for hyrox`, `hyrox training plan` | `hyrox` ≈ 22 и резкий рост в сентябре 2026; PureGym +171 %; 49 500/мес (+22 %) | Fitness Race: 8 × 1 km (8 нед × 3). Решение по бренду: план без торговых марок, в статье допустимо «races such as Hyrox» — согласовать | training | ⏳ | ★★ |
| 28 | Starting to Run After 50 (or 40): First 5K and Strong Runs | `running after 50 women` / `men` / `knees` / `how to start`, `running for beginners over 50` / `over 40` | два кластера; Garmin: 30–39 — самая быстрорастущая группа → добавить угол «после 40» | First 5K After 50 (12 нед × 3), Strong Runs at 50+ (8 нед × 3); дисклеймер «training advice, not medical advice» | training | ⏳ | ★★ |
| 29 | First 50K: Training for Your First Ultra | `ultramarathon training plan 50k`, `ultramarathon training app` | PureGym: ultra-планы +50 %; ITRA 3,45 млн атлетов с индексом | First 50K (16 нед × 4) | training | ⏳ | ★ |
| 30 | Winter Running Guide: Dark, Cold, Treadmill | `running in winter tips` / `what to wear`, `treadmill workout plan`, `how to start running on a treadmill` | Garmin: дорожка +12,6 %; сезонный запрос — публиковать в начале ноября | Dark mode, Indoor-режим, Winter Treadmill Plan, 8 пресетов Treadmill | guides | ⏳ | ★★ |

### 4.3 Что сознательно не берём

- Медицинское без привязки к приложению: `shin splints`, `runner's knee`, `is running bad for your knees`, `running injuries`.
- Тренды без функции под них: `tai chi walking`, `walking yoga`, `plank hover`, `running app that pays you`.
- `running cadence` как отдельная тема — автодополнение забито армейскими «cadence songs»; оставить абзацем в статье про форму бега.
- Бренд «Hyrox» в заголовках (см. #27).

### 4.4 Бэклог с подтверждённым интересом (не вошли в 30)

Tempo vs Threshold (`what is tempo pace`, `threshold run vs tempo run` — автодополнение богатое, Trends ≈ 1) · Trek Ready / `hiking training plan on treadmill` (хайкинг-клубы 5,8×) · Postnatal Return (`running after pregnancy pelvic floor`) · Walk a Half Marathon · Faster Mile · First 15K · Camino · 30-Minute Runner.

## 5. Не статьи, а инструменты

Слово `calculator` есть в 11 кластерах: `zone 2 running calculator`, `heart rate zones running calculator`, `easy run pace calculator`, `tempo run calculator`, `running pace calculator`, `running cadence calculator`, `run walk method calculator`, `jeffing calculator`, `rucking calorie calculator`, `incline walking calorie calculator`, `walking for weight loss calculator`. Три страницы-калькулятора на сайте закрыли бы большинство без медицинских обещаний:

1. **Heart-rate zones / Zone 2 calculator** — по возрасту или по max HR, с теми же границами зон, что в приложении.
2. **Pace calculator** — темп ↔ скорость, км ↔ мили, easy/tempo/race pace по результату на 5K.
3. **Run-walk calculator** — соотношение бег/ходьба и итоговый темп на дистанцию.

Каждый калькулятор ведёт на соответствующий план и статью (#2, #9, #10, #26).

## 6. Сезонный календарь публикаций

| Когда | Что | Почему |
|---|---|---|
| сентябрь–октябрь | #17 half plan, #18 first marathon, #27 fitness racing, #16 trail | пик `half/marathon training plan` в октябре; `hyrox` растёт сейчас |
| ноябрь | #30 winter guide, #21 12-3-30 (если 1.2.2 вышла), treadmill-темы | Garmin: дорожка +12,6 % |
| декабрь–январь | #5 couch to 5K, #4 start from zero, #6 free app, #7 Strava alternatives, #15 run every day | январский пик `couch to 5k`, `strava`, всех «план»-запросов |
| март–июнь | #2, #9 zone 2, #14 walk vs run, #21 12-3-30, #25 rucking | пик `zone 2` март–июнь, `12 3 30` и `japanese walking` летом |

## 7. Источники

- Google Trends (US, 12 мес): [japanese walking / zone 2 running / rucking / 12 3 30 / couch to 5k](https://trends.google.com/trends/explore?date=today%2012-m&geo=US&q=japanese%20walking,zone%202%20running,rucking,12%203%2030,couch%20to%205k), [планы](https://trends.google.com/trends/explore?date=today%2012-m&geo=US&q=couch%20to%205k,half%20marathon%20training%20plan,marathon%20training%20plan,10k%20training%20plan,5k%20training%20plan), [типы тренировок](https://trends.google.com/trends/explore?date=today%2012-m&geo=US&q=interval%20running,tempo%20run,zone%202,run%20walk%20method,hyrox), [приложения](https://trends.google.com/trends/explore?date=today%2012-m&geo=US&q=running%20app,strava,nike%20run%20club,runna,running%20app%20territory)
- Google Autocomplete: `scratchpad/kw/suggest.json`, `suggest2.json` (117 сидов, снято 2026-09-16)
- [Strava — 12th annual Year in Sport trend report (2025)](https://press.strava.com/articles/strava-releases-12th-annual-year-in-sport-trend-report-2025)
- [Garmin — Trends in Running 2026](https://www.garmin.com/en-GB/blog/trends-in-running-new-data-shows-how-garmin-runners-hit-their-stride/)
- [PureGym — UK Fitness Report 2025/26](https://www.puregym.com/blog/uk-fitness-report-gym-statistics/); обзор роста поисков — [Athletech News](https://athletechnews.com/fitness-trends-2026-walking-workouts-google-data/)
- [risingtrends.co — sports trends 2026](https://www.risingtrends.co/trends/sports-trends-2026)
- [SGI Europe — Running: state of play 2026](https://www.sgieurope.com/consumer/running-state-of-play-2026/122512.article)
- [Dexerto — INTVL, territory-приложение](https://www.dexerto.com/gaming/new-running-app-turns-your-neighborhood-into-a-real-life-civ-7-game-3389630/)
