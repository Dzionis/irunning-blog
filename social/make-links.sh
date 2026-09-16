#!/bin/bash
# Usage: ./make-links.sh <PROVIDER_TOKEN>   → rewrites links.md
# Provider token: App Store Connect → App Analytics → Acquisition → Campaigns →
# "Generate Campaign Link" → the pt=… number in the generated link.
set -euo pipefail
cd "$(dirname "$0")"
PT="${1:-PT_TOKEN}"
APP="https://apps.apple.com/app/apple-store/id6770997508"
SITE="https://irunning.app/"
{
  echo "# Ссылки по источникам"
  echo
  echo "Сгенерировано \`make-links.sh\` из \`links.tsv\`. Provider token: \`$PT\`."
  [ "$PT" = "PT_TOKEN" ] && echo && echo "> ⚠️ Токен ещё не подставлен. Запусти \`./make-links.sh 123456\` с числом pt из App Store Connect, иначе установки не атрибутируются."
  echo
  echo "**App Store** — установки видны в App Store Connect → App Analytics → Acquisition → Campaigns (по \`ct\`)."
  echo "**Блог** — визиты видны в GA4 → Acquisition → Traffic acquisition (source / campaign); клик в App Store со страницы блога получит \`ct=web-<source>\`."
  echo
  echo "| Канал | Где ставить | App Store | Блог |"
  echo "|---|---|---|---|"
  grep -v '^#' links.tsv | while IFS=$'\t' read -r ch place ct src camp; do
    echo "| $ch | $place | \`$APP?pt=$PT&ct=$ct&mt=8\` | \`${SITE}?utm_source=$src&utm_medium=social&utm_campaign=$camp\` |"
  done
  echo
  echo "Для конкретной статьи: взять её URL и добавить тот же хвост \`?utm_source=…&utm_medium=social&utm_campaign=…\`."
  echo "Новый источник: добавить строку в \`links.tsv\` и перезапустить скрипт. \`ct\` — не длиннее 40 символов."
} > links.md
if [ "$PT" != "PT_TOKEN" ]; then
  sed -i '' "s/var PROVIDER_TOKEN = '[0-9]*';/var PROVIDER_TOKEN = '$PT';/" ../assets/js/analytics.js
  echo "set PROVIDER_TOKEN in assets/js/analytics.js"
fi
echo "wrote links.md (pt=$PT)"
