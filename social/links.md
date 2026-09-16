# Ссылки по источникам

Сгенерировано `make-links.sh` из `links.tsv`. Provider token: `1239441`.

**App Store** — установки видны в App Store Connect → App Analytics → Acquisition → Campaigns (по `ct`).
**Блог** — визиты видны в GA4 → Acquisition → Traffic acquisition (source / campaign); клик в App Store со страницы блога получит `ct=web-<source>`.

| Канал | Где ставить | App Store | Блог |
|---|---|---|---|
| Instagram | bio link | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=ig-bio&mt=8` | `https://irunning.app/?utm_source=instagram&utm_medium=social&utm_campaign=bio` |
| Instagram | stories link sticker | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=ig-story&mt=8` | `https://irunning.app/?utm_source=instagram&utm_medium=social&utm_campaign=story` |
| Instagram | reel / post caption | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=ig-post&mt=8` | `https://irunning.app/?utm_source=instagram&utm_medium=social&utm_campaign=post` |
| Threads | bio link | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=th-bio&mt=8` | `https://irunning.app/?utm_source=threads&utm_medium=social&utm_campaign=bio` |
| Threads | post link | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=th-post&mt=8` | `https://irunning.app/?utm_source=threads&utm_medium=social&utm_campaign=post` |
| Facebook | page button + about | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=fb-page&mt=8` | `https://irunning.app/?utm_source=facebook&utm_medium=social&utm_campaign=page` |
| Facebook | page post | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=fb-post&mt=8` | `https://irunning.app/?utm_source=facebook&utm_medium=social&utm_campaign=post` |
| Facebook | groups | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=fb-group&mt=8` | `https://irunning.app/?utm_source=facebook&utm_medium=social&utm_campaign=group` |
| TikTok | bio link | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=tt-bio&mt=8` | `https://irunning.app/?utm_source=tiktok&utm_medium=social&utm_campaign=bio` |
| YouTube | Shorts description / channel | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=yt-shorts&mt=8` | `https://irunning.app/?utm_source=youtube&utm_medium=social&utm_campaign=shorts` |
| Reddit | profile social link | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=rd-profile&mt=8` | `https://irunning.app/?utm_source=reddit&utm_medium=social&utm_campaign=profile` |
| Reddit | comments / answers | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=rd-comment&mt=8` | `https://irunning.app/?utm_source=reddit&utm_medium=social&utm_campaign=comment` |
| Reddit | own posts | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=rd-post&mt=8` | `https://irunning.app/?utm_source=reddit&utm_medium=social&utm_campaign=post` |
| Reddit | giveaway posts | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=rd-giveaway&mt=8` | `https://irunning.app/?utm_source=reddit&utm_medium=social&utm_campaign=giveaway` |
| X | bio | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=x-bio&mt=8` | `https://irunning.app/?utm_source=x&utm_medium=social&utm_campaign=bio` |
| X | posts / threads | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=x-post&mt=8` | `https://irunning.app/?utm_source=x&utm_medium=social&utm_campaign=post` |
| Pinterest | pins | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=pin-pin&mt=8` | `https://irunning.app/?utm_source=pinterest&utm_medium=social&utm_campaign=pin` |
| Pinterest | profile | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=pin-profile&mt=8` | `https://irunning.app/?utm_source=pinterest&utm_medium=social&utm_campaign=profile` |
| Email | signature / DMs | `https://apps.apple.com/app/apple-store/id6770997508?pt=1239441&ct=dm&mt=8` | `https://irunning.app/?utm_source=direct&utm_medium=social&utm_campaign=dm` |

Для конкретной статьи: взять её URL и добавить тот же хвост `?utm_source=…&utm_medium=social&utm_campaign=…`.
Новый источник: добавить строку в `links.tsv` и перезапустить скрипт. `ct` — не длиннее 40 символов.
