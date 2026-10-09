// Uso: sirva o site com "python3 video/captura/servidor.py <pasta do site> 8771" e rode
// "NODE_PATH=$(npm root -g) node video/captura/computador.js 18.5 saida.mp4" (o Playwright já vem na nuvem do Claude Code).
// Gravação do site no computador (1280 × 800, saída 1440 × 900) para a janela do vídeo da Nortiq.
const { gravar } = require('./motor');
const CURSOR = '.cursor{width:16px!important;height:16px!important;margin:-8px 0 0 -8px!important;box-shadow:0 0 0 2px rgba(28,14,18,.35)}.cursor-ring{border-width:2px!important;border-color:rgba(201,160,99,.9)!important}';
const DUR = +(process.argv[2] || 17);
(async () => {
  await gravar({
    nome: 'computador', url: 'http://127.0.0.1:8771/', viewport: { width: 1280, height: 800 }, dpr: 1.5, escala: '1440:900',
    duracao: DUR, saida: process.argv[3] || 'computador.mp4', mouseInicial: { x: 820, y: 600 },
    antes: (page) => page.addStyleTag({ content: CURSOR }),
    acoes: [
      // início: a abertura do site e o título
      { t: 3.2, mover: '.nav-links a[href="#portfolio"]', dur: 0.9 },
      { t: 4.3, clicar: true },
      { t: 4.95, real: 900 },                                   // cortina fechada: dá tempo das fotos carregarem
      // portfólio: filtra Nail art e abre uma foto
      { t: 6.0, mover: { sel: '#pfFilters button', texto: 'Nail art' }, dur: 0.7 },
      { t: 6.85, clicar: true },
      { t: 7.45, mover: '.pf-item[data-idx="8"]', dur: 0.85 },
      { t: 8.55, clicar: true },
      { t: 8.7, real: 600 },
      { t: 9.0, mover: '#lbUse', dur: 0.7 },
      { t: 9.85, clicar: true },
      { t: 10.5, real: 1200 },                                  // cortina fechada: carrega a mão e a referência
      // Monte sua unha: copia a cor da foto, troca o formato, o comprimento e o acabamento e envia
      { t: 12.2, mover: { expr: "(() => { const r = document.querySelector('#pickerArea').getBoundingClientRect(); const k = Math.min(r.width / 562, r.height / 1000); return { x: r.left + (r.width - 562 * k) / 2 + 105 * k, y: r.top + (r.height - 1000 * k) / 2 + 455 * k }; })()" }, dur: 0.7 },
      { t: 13.1, clicar: true },
      { t: 13.5, mover: 'label.chip:has(input[value=stiletto])', dur: 0.55 },
      { t: 14.1, clicar: true },
      { t: 14.4, mover: 'label.chip:has(input[value=longa])', dur: 0.45 },
      { t: 14.95, clicar: true },
      { t: 15.2, mover: 'label.chip:has(input[value=glitter])', dur: 0.5 },
      { t: 15.8, clicar: true },
      { t: 16.1, roda: 520, dur: 0.7 },
      { t: 17.1, mover: '#simSend', dur: 0.5 },
      { t: 17.7, clicar: true },
    ],
  });
})().catch((e) => { console.error(e); process.exit(1); });
