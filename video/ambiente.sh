# Prepara o ambiente para montar e renderizar os vídeos do Nortiq (HyperFrames).
# Uso: source video/ambiente.sh
# - instala o ffmpeg e o numpy/scipy (trilha) se faltarem;
# - aponta o HyperFrames para o Chromium já instalado na nuvem do Claude Code (em outra máquina, ele usa o próprio).
command -v ffmpeg >/dev/null 2>&1 || { apt-get update -qq && apt-get install -y -qq ffmpeg >/dev/null; }
python3 -c "import numpy, scipy" 2>/dev/null || pip install -q numpy scipy
for b in /opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell; do
  [ -x "$b" ] && export HYPERFRAMES_BROWSER_PATH="$b"
done
export HYPERFRAMES_NO_TELEMETRY=1 HYPERFRAMES_NO_UPDATE_CHECK=1 HYPERFRAMES_SKIP_SKILLS=1
export HF="npx --yes hyperframes@0.8.114"
echo "ambiente pronto: ffmpeg $(ffmpeg -version | head -1 | cut -d' ' -f3), navegador ${HYPERFRAMES_BROWSER_PATH:-padrão do HyperFrames}"
