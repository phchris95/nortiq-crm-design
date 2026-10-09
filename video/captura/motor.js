// Grava um site quadro a quadro, com o tempo controlado: o resultado sai liso a 30 quadros por segundo,
// mesmo que a máquina seja lenta. O relógio da página é falso (GSAP, Lenis, timers), as animações de CSS
// são posicionadas pelo Web Animations API e os vídeos são buscados quadro a quadro.
const { chromium } = require('playwright');
const { spawn } = require('child_process');

const SINCRONIA = `
(() => {
  const P = HTMLMediaElement.prototype;
  P.play = function () {
    if (!this.__quer) { this.__quer = true; this.__de = this.currentTime || 0; this.__ini = undefined; this.__avisou = false; }
    if (this.readyState === 0 && this.networkState !== 2) { try { this.preload = 'auto'; this.load(); } catch (e) {} }
    return Promise.resolve();
  };
  P.pause = function () { if (this.__quer) { this.__quer = false; this.__ini = undefined; } };
  Object.defineProperty(P, 'paused', { get() { return !this.__quer; }, configurable: true });

  window.__sync = async (agora) => {
    for (const a of document.getAnimations()) {
      if (a.__ini === undefined) a.__ini = agora - (a.currentTime || 0);
      const ct = agora - a.__ini;
      const fim = a.effect ? a.effect.getComputedTiming().endTime : Infinity;
      if (isFinite(fim) && ct >= fim) { try { a.finish(); } catch (e) {} continue; }
      try { if (a.playState !== 'paused') a.pause(); a.currentTime = ct; } catch (e) {}
    }
    const esperas = [];
    for (const v of document.querySelectorAll('video')) {
      if (v.__quer && v.readyState < 2 && v.currentSrc) {
        await new Promise((ok) => { v.addEventListener('loadeddata', ok, { once: true }); setTimeout(ok, 5000); });
      }
      if (!v.__quer || !(v.readyState >= 1) || !isFinite(v.duration) || !v.duration) continue;
      if (v.__ini === undefined) v.__ini = agora - v.__de * 1000;
      let alvo = (agora - v.__ini) / 1000;
      alvo = v.loop ? alvo % v.duration : Math.min(alvo, v.duration - 0.01);
      if (Math.abs(v.currentTime - alvo) > 0.001) {
        esperas.push(new Promise((ok) => { const f = () => ok(); v.addEventListener('seeked', f, { once: true }); setTimeout(f, 1500); }));
        v.currentTime = alvo;
      }
      if (!v.__avisou && v.readyState >= 2) { v.__avisou = true; v.dispatchEvent(new Event('playing')); }
    }
    await Promise.all(esperas);
  };

  // Toque ou clique visível no vídeo (só para a gravação; o site não tem isso)
  window.__toque = (x, y, cor) => {
    const d = document.createElement('div');
    d.style.cssText = 'position:fixed;left:' + (x - 28) + 'px;top:' + (y - 28) + 'px;width:56px;height:56px;border-radius:50%;' +
      'border:3px solid ' + cor + ';background:' + cor.replace(')', ',0.18)').replace('rgb(', 'rgba(') + ';pointer-events:none;z-index:2147483647';
    document.documentElement.appendChild(d);
    const a = d.animate([{ transform: 'scale(0.45)', opacity: 0.95 }, { transform: 'scale(1.35)', opacity: 0 }], { duration: 520, easing: 'cubic-bezier(.2,.7,.3,1)', fill: 'forwards' });
    a.onfinish = () => d.remove();
  };
})();
`;

const suave = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);

async function centro(page, alvo) {
  if (Array.isArray(alvo)) return { x: alvo[0], y: alvo[1] };
  if (alvo && alvo.expr) return page.evaluate(alvo.expr);
  const r = await page.evaluate((sel) => {
    let el = null;
    if (typeof sel === 'string') el = document.querySelector(sel);
    else if (sel && sel.sel) el = Array.from(document.querySelectorAll(sel.sel)).filter((e) => e.offsetParent !== null).find((e) => !sel.texto || e.textContent.includes(sel.texto)) || null;
    if (!el) return null;
    const b = el.getBoundingClientRect();
    return { x: b.left + b.width / 2, y: b.top + b.height / 2 };
  }, alvo);
  if (!r) throw new Error('não achei ' + alvo);
  return r;
}

async function gravar(o) {
  const fps = o.fps || 30;
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    viewport: o.viewport, deviceScaleFactor: o.dpr || 1, isMobile: !!o.mobile, hasTouch: !!o.mobile,
    timezoneId: 'America/Sao_Paulo', locale: 'pt-BR', reducedMotion: 'no-preference',
  });
  const page = await ctx.newPage();
  const erros = [];
  page.on('pageerror', (e) => erros.push(e.message));
  await page.addInitScript(SINCRONIA);
  const inicio = new Date(o.relogio || '2026-10-09T10:00:00-03:00').getTime();
  await page.clock.install({ time: inicio });
  await page.clock.pauseAt(inicio + 1);
  await page.goto(o.url, { waitUntil: 'load' });
  await page.waitForTimeout(o.esperaInicial || 1500);
  if (o.antes) await o.antes(page);

  const saida = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    ...(o.escala ? ['-vf', `scale=${o.escala}:flags=lanczos`] : []),
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '14', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', o.saida], { stdio: ['pipe', 'inherit', 'inherit'] });

  const acoes = o.acoes.slice().sort((a, b) => a.t - b.t);
  let mouse = o.mouseInicial ? { ...o.mouseInicial } : { x: o.viewport.width / 2, y: o.viewport.height / 2 };
  await page.mouse.move(mouse.x, mouse.y);
  let mov = null, rolagem = null, prox = 0;
  const N = Math.round(o.duracao * fps);

  for (let i = 0; i < N; i++) {
    const t = i / fps;
    while (prox < acoes.length && acoes[prox].t <= t + 1e-6) {
      const a = acoes[prox++];
      if (a.mover) { const d = await centro(page, a.mover); mov = { de: { ...mouse }, para: { x: d.x + (a.dx || 0), y: d.y + (a.dy || 0) }, t0: a.t, dur: a.dur || 0.8 }; }
      if (a.clicar) {
        await page.evaluate(([x, y, c]) => window.__toque(x, y, c), [mouse.x, mouse.y, o.corToque || 'rgb(201,160,99)']);
        await page.mouse.down(); await page.mouse.up();
      }
      if (a.tocar) {
        const d = await centro(page, a.tocar);
        await page.evaluate(([x, y, c]) => window.__toque(x, y, c), [d.x, d.y, o.corToque || 'rgb(201,160,99)']);
        await page.touchscreen.tap(d.x, d.y);
      }
      if (a.rolar !== undefined) {
        const de = await page.evaluate(() => window.scrollY);
        let para = a.rolar;
        if (typeof a.rolar === 'string') para = await page.evaluate(([sel, off]) => { const el = document.querySelector(sel); return el.getBoundingClientRect().top + window.scrollY + off; }, [a.rolar, a.off || 0]);
        rolagem = { de, para, t0: a.t, dur: a.dur || 1 };
      }
      if (a.roda) { rolagem = { roda: a.roda, t0: a.t, dur: a.dur || 0.8, feito: 0 }; }
      if (a.real) await page.waitForTimeout(a.real);
      if (a.js) await page.evaluate(a.js);
    }
    if (mov) {
      const k = Math.min(1, (t - mov.t0) / mov.dur);
      const e = suave(Math.max(0, k));
      // um leve arco deixa o movimento do mouse mais humano
      const arco = Math.sin(Math.PI * e) * (mov.arco ?? 0.06) * Math.hypot(mov.para.x - mov.de.x, mov.para.y - mov.de.y);
      const nx = mov.de.x + (mov.para.x - mov.de.x) * e, ny = mov.de.y + (mov.para.y - mov.de.y) * e - arco;
      if (Math.abs(nx - mouse.x) > 0.01 || Math.abs(ny - mouse.y) > 0.01) { mouse = { x: nx, y: ny }; await page.mouse.move(nx, ny); }
      if (k >= 1) mov = null;
    }
    if (rolagem) {
      const k = Math.min(1, (t - rolagem.t0) / rolagem.dur);
      if (rolagem.roda !== undefined) {
        const alvo = rolagem.roda * suave(Math.max(0, k)), passo = alvo - rolagem.feito;
        if (Math.abs(passo) >= 1) { await page.mouse.wheel(0, passo); rolagem.feito += passo; }
      } else {
        const y = rolagem.de + (rolagem.para - rolagem.de) * suave(Math.max(0, k));
        await page.evaluate((y) => window.scrollTo(0, y), y);
      }
      if (k >= 1) rolagem = null;
    }
    await page.clock.runFor(1000 / fps);
    await page.evaluate((n) => window.__sync(n), (i + 1) * 1000 / fps);
    const img = await page.screenshot({ type: 'jpeg', quality: 94 });
    if (!saida.stdin.write(img)) await new Promise((ok) => saida.stdin.once('drain', ok));
    if (i % 60 === 0) process.stdout.write(`  ${o.nome}: ${(t).toFixed(1)} s\n`);
  }
  saida.stdin.end();
  await new Promise((ok) => saida.on('close', ok));
  await browser.close();
  if (erros.length) console.log('erros na página:', erros);
  console.log('pronto:', o.saida);
}

module.exports = { gravar };
