#!/usr/bin/env bash
# Leva o som do vídeo a -16 LUFS e pico de -1,5 dB (duas passadas, ganho linear: não muda a mistura).
# A imagem é copiada sem recodificar. Uso: bash video/finalizar.sh entrada.mp4 saida.mp4
set -euo pipefail
ENTRADA="$1"; SAIDA="$2"
MEDIDA=$(ffmpeg -hide_banner -nostats -i "$ENTRADA" -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
read -r I TP LRA LIMIAR DESVIO < <(echo "$MEDIDA" | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['input_i'],d['input_tp'],d['input_lra'],d['input_thresh'],d['target_offset'])")
ffmpeg -v error -y -i "$ENTRADA" -c:v copy \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=$I:measured_TP=$TP:measured_LRA=$LRA:measured_thresh=$LIMIAR:offset=$DESVIO:linear=true,aresample=48000" \
  -c:a aac -b:a 192k -movflags +faststart "$SAIDA"
echo "$SAIDA (entrada: $I LUFS)"
ffmpeg -hide_banner -nostats -i "$SAIDA" -af ebur128=peak=true -f null - 2>&1 | grep -A14 Summary | grep -E "I:|Peak:"
