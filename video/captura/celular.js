// Uso: igual ao computador.js: "NODE_PATH=$(npm root -g) node video/captura/celular.js 16.2 saida.mp4".
// Gravação do site no celular (390 × 845, saída 852 × 1846) para os vídeos da Salure.
const { gravar } = require('./motor');
const DUR = +(process.argv[2] || 16);
(async () => {
  await gravar({
    nome: 'celular', url: 'http://127.0.0.1:8771/', viewport: { width: 390, height: 845 }, dpr: 3, mobile: true, escala: '852:1846',
    duracao: DUR, saida: process.argv[3] || 'celular.mp4', corToque: 'rgb(201,160,99)',
    acoes: [
      { t: 3.0, rolar: 1500, dur: 1.9 },
      { t: 5.2, tocar: '#burger' },
      { t: 6.0, tocar: '#menu a[href="#portfolio"]' },
      { t: 6.6, real: 900 },
      { t: 7.6, rolar: 700, dur: 1.2 },
      { t: 9.1, tocar: '#burger' },
      { t: 9.9, tocar: '#menu a[href="#monte-sua-unha"]' },
      { t: 10.5, real: 1300 },
      { t: 11.6, rolar: '#stage', off: -80, dur: 0.8 },
      { t: 12.6, tocar: 'label.chip:has(input[value=stiletto])' },
      { t: 13.3, tocar: 'button[data-tab=cor]' },
      { t: 13.8, tocar: '#colorSwatches > :nth-child(4)' },
      { t: 14.4, tocar: 'button[data-tab=acabamento]' },
      { t: 14.9, tocar: 'label.chip:has(input[value=francesinha])' },
    ],
  });
})().catch((e) => { console.error(e); process.exit(1); });
