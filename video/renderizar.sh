#!/usr/bin/env bash
# Confere, renderiza e finaliza as duas versões do vídeo (site 16:9 e Instagram 9:16).
# Uso: bash video/renderizar.sh
# Resultado em video/finais/: o som de cada vídeo é levado a -16 LUFS (padrão de celular e redes),
# sem mudar o equilíbrio entre a trilha e os efeitos.
set -euo pipefail
AQUI="$(cd "$(dirname "$0")" && pwd)"
source "$AQUI/ambiente.sh"

for v in site-16x9 instagram-9x16; do
  echo "== $v"
  (cd "$AQUI/$v" && $HF check && $HF render -o "renders/nortiq-$v.mp4")
  bash "$AQUI/finalizar.sh" "$AQUI/$v/renders/nortiq-$v.mp4" "$AQUI/finais/nortiq-$v.mp4"
done
