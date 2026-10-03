# Trilha instrumental original do vídeo Nortiq (sem samples de terceiros). Uso: python3 video/trilha/trilha.py
# 108 BPM, 7 compassos + cauda = 16 s. "Modern corporate / upbeat tech": batida leve, baixo, arpejo
# discreto e pad. Compasso 1 (abertura) sem bateria; a batida entra no corte para Orçamentos (2,222 s);
# compasso 7 (encerramento) resolve em Dó e some.
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
BPM = 108
B = 60 / BPM            # tempo (0,5556 s)
S16 = B / 4             # semicolcheia
BAR = 4 * B
DUR = 16.0
N = int(SR * DUR)
rng = np.random.default_rng(108)


def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def polyblep(t, dt):
    out = np.zeros_like(t)
    m = t < dt
    x = t[m] / dt
    out[m] = x + x - x * x - 1.0
    m = t > 1.0 - dt
    x = (t[m] - 1.0) / dt
    out[m] = x * x + x + x + 1.0
    return out


def saw(freq, n, phase0=0.0):
    dt = freq / SR
    ph = (phase0 + dt * np.arange(n)) % 1.0
    return (2.0 * ph - 1.0) - polyblep(ph, dt)


def lowpass(x, fc, order=2):
    fc = min(fc, SR * 0.45)
    b, a = signal.butter(order, fc / (SR / 2), 'low')
    return signal.lfilter(b, a, x)


def highpass(x, fc, order=2):
    b, a = signal.butter(order, fc / (SR / 2), 'high')
    return signal.lfilter(b, a, x)


def bandpass(x, lo, hi, order=2):
    b, a = signal.butter(order, [lo / (SR / 2), hi / (SR / 2)], 'band')
    return signal.lfilter(b, a, x)


class Bus:
    def __init__(self):
        self.L = np.zeros(N)
        self.R = np.zeros(N)

    def add(self, t, sig, gain=1.0, pan=0.0, sigR=None):
        i = int(round(t * SR))
        if i >= N:
            return
        a = (pan + 1) * np.pi / 4
        right = sig if sigR is None else sigR
        n = min(len(sig), N - i)
        self.L[i:i + n] += sig[:n] * gain * np.cos(a) * np.sqrt(2)
        self.R[i:i + n] += right[:n] * gain * np.sin(a) * np.sqrt(2)


drums, bass, arp, pad, fx = Bus(), Bus(), Bus(), Bus(), Bus()
sends = Bus()  # para o reverb

# ---------------------------------------------------------------- harmonia (um acorde por compasso)
CHORDS = [  # (fundamental do baixo, notas do pad)
    (36, [60, 64, 67, 74]),   # C add9   (abertura)
    (41, [60, 65, 67, 69]),   # F add9   (orçamentos)
    (43, [62, 67, 69, 71]),   # G6/9
    (45, [60, 64, 67, 69]),   # Am7      (clientes)
    (41, [60, 65, 67, 69]),   # F add9   (agenda)
    (43, [62, 67, 69, 71]),   # G6/9     (metas)
    (36, [60, 64, 67, 72]),   # C        (encerramento)
]
DRUM_IN = 1 * BAR          # 2,222 s
END_BAR = 6 * BAR          # 13,333 s

# ---------------------------------------------------------------- bateria
def kick(vel=1.0):
    n = int(0.42 * SR)
    t = np.arange(n) / SR
    f = 46 + 95 * np.exp(-t / 0.035)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t / 0.22)
    click = rng.standard_normal(n) * np.exp(-t / 0.004) * 0.25
    return (body + highpass(click, 1500)) * vel


def clap(vel=1.0):
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    noise = bandpass(rng.standard_normal(n), 900, 6000)
    env = np.zeros(n)
    for k, d in enumerate([0.0, 0.011, 0.022]):
        env += (t >= d) * np.exp(-np.clip(t - d, 0, None) / (0.006 if k < 2 else 0.12))
    tone = np.sin(2 * np.pi * 210 * t) * np.exp(-t / 0.03) * 0.3
    return (noise * env * 0.6 + tone) * vel


def hat(vel=1.0, open_=False):
    n = int((0.32 if open_ else 0.07) * SR)
    t = np.arange(n) / SR
    x = lowpass(highpass(rng.standard_normal(n), 7500, 3), 13000)
    return x * np.exp(-t / (0.11 if open_ else 0.018)) * vel


def crash(vel=1.0, dur=1.6):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = highpass(rng.standard_normal(n), 4500, 2)
    return x * np.exp(-t / (dur / 3.2)) * vel


KICK_STEPS = {0: 1.0, 6: 0.55, 8: 0.9}
kicks = []
for bar in range(1, 6):
    t0 = bar * BAR
    for st in range(16):
        t = t0 + st * S16
        if st in KICK_STEPS:
            drums.add(t, kick(KICK_STEPS[st]), 0.72)
            kicks.append((t, KICK_STEPS[st]))
        if st in (4, 12):
            c = clap(0.8)
            drums.add(t, c, 0.42, pan=0.05)
            sends.add(t, c, 0.18)
        if st % 4 == 2:                       # contratempo
            drums.add(t, hat(0.55), 0.35, pan=0.25)
        elif st % 2 == 1:                      # semicolcheias bem leves
            drums.add(t, hat(0.25), 0.3, pan=-0.2)
        if st == 14 and bar in (2, 4):         # abertura de chimbal antes do compasso seguinte
            drums.add(t, hat(0.5, open_=True), 0.3, pan=0.25)
# Compasso 1: shaker discreto a partir do segundo tempo, crescendo.
for st in range(4, 16):
    v = 0.12 + 0.18 * (st - 4) / 12
    drums.add(st * S16, hat(v), 0.35, pan=(-0.25 if st % 2 else 0.25))
# Entrada da bateria e o fim com prato.
drums.add(DRUM_IN, crash(0.32), 0.5, pan=-0.1)
drums.add(END_BAR, kick(1.0), 0.75)
kicks.append((END_BAR, 1.0))
drums.add(END_BAR, crash(0.36, 2.4), 0.5, pan=0.1)
sends.add(END_BAR, crash(0.36, 2.4), 0.15)
# Swell reverso de ruído chegando no corte da abertura.
n = int(0.75 * SR)
sw = bandpass(rng.standard_normal(n), 2500, 9000) * np.linspace(0, 1, n) ** 2.2
fx.add(DRUM_IN - 0.75, sw, 0.16)

# ---------------------------------------------------------------- baixo (colcheias, a partir do compasso 2)
def bass_note(m, dur, vel=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = mtof(m)
    x = saw(f, n) * 0.6 + np.sin(2 * np.pi * f * t) * 0.9
    x = lowpass(x, 520 + 900 * vel * np.exp(-0.0) , 2)
    env = np.minimum(1, t / 0.004) * np.exp(-t / (dur * 0.9))
    rel = np.ones(n)
    k = int(0.02 * SR)
    rel[-k:] = np.linspace(1, 0, k)
    return x * env * rel * vel


for bar in range(1, 6 + 1):
    root = CHORDS[bar][0]
    if bar == 6:
        bass.add(bar * BAR, bass_note(root, 2.6, 1.0), 0.75)
        break
    for st in range(0, 16, 2):
        m = root + (12 if st in (6, 14) else 0)
        bass.add(bar * BAR + st * S16, bass_note(m, S16 * 1.7, 0.95 if st % 8 == 0 else 0.8), 0.75)

# ---------------------------------------------------------------- arpejo (semicolcheias, discreto)
PATTERN = [0, 2, 1, 3, 2, 1, 3, 2]
for bar in range(7):
    notes = sorted(n + 12 for n in CHORDS[bar][1])
    steps = 16 if bar < 6 else 12
    for st in range(steps):
        t = bar * BAR + st * S16
        m = notes[PATTERN[st % 8]]
        n = int(0.3 * SR)
        tt = np.arange(n) / SR
        f = mtof(m)
        x = saw(f * 1.003, n) * 0.5 + saw(f * 0.997, n) * 0.5
        # Abertura: o filtro abre aos poucos; no fim, fecha e some.
        if bar == 0:
            fc = 700 + 2600 * (st / 15) ** 1.6
            vel = 0.55 + 0.35 * st / 15
        elif bar == 6:
            fc = 3000 - 2200 * (st / 11)
            vel = 0.85 * (1 - st / 13)
        else:
            fc = 3300
            vel = 0.95 if st % 4 == 0 else 0.7
        x = lowpass(x, fc, 2)
        env = np.minimum(1, tt / 0.002) * np.exp(-tt / 0.085)
        pan = 0.35 if st % 2 else -0.35
        arp.add(t, x * env, (0.36 if bar == 0 else 0.3) * vel, pan=pan)
        sends.add(t, x * env, 0.07 * vel)

# Eco (colcheia pontuada) só no arpejo, alternando lados.
d = int(round(3 * S16 * SR))
eL, eR = np.zeros(N), np.zeros(N)
eL[d:] += arp.R[:-d] * 0.32
eR[d:] += arp.L[:-d] * 0.32
eL[2 * d:] += arp.L[:-2 * d] * 0.12
eR[2 * d:] += arp.R[:-2 * d] * 0.12
arp.L += lowpass(eL, 2500)
arp.R += lowpass(eR, 2500)

# ---------------------------------------------------------------- pad (camada de fundo)
for bar in range(7):
    notes = CHORDS[bar][1]
    start = bar * BAR - (0.05 if bar else 0)
    dur = BAR + 0.5 if bar < 6 else DUR - start
    n = int(dur * SR)
    t = np.arange(n) / SR
    L = np.zeros(n)
    R = np.zeros(n)
    for m in notes:
        f = mtof(m)
        for cents, side in ((-8, 0), (0, 2), (8, 1)):
            w = saw(f * 2 ** (cents / 1200), n, rng.random())
            if side in (0, 2):
                L += w
            if side in (1, 2):
                R += w
    att = 0.35 if bar else 0.12
    env = np.minimum(1, t / att)
    rel = np.ones(n)
    k = int(0.45 * SR)
    rel[-k:] = np.linspace(1, 0, k) ** 1.5
    L = lowpass(L, 1500, 2) * env * rel
    R = lowpass(R, 1500, 2) * env * rel
    g = 0.07 if bar else 0.1
    pad.add(start, L, g, sigR=R)
    sends.add(start, (L + R) * 0.5, 0.02)

# ---------------------------------------------------------------- sidechain leve (baixo e pad respiram com o bumbo)
duck = np.ones(N)
tt = np.arange(N) / SR
for t, v in kicks:
    i = int(t * SR)
    seg = tt[i:i + int(0.3 * SR)] - t
    duck[i:i + len(seg)] = np.minimum(duck[i:i + len(seg)], 1 - 0.32 * v * np.exp(-seg / 0.09))
for bus in (bass, pad):
    bus.L *= duck
    bus.R *= duck

# ---------------------------------------------------------------- reverb (ruído com decaimento, estéreo)
ir_n = int(1.5 * SR)
ti = np.arange(ir_n) / SR
irL = rng.standard_normal(ir_n) * np.exp(-ti / 0.38)
irR = rng.standard_normal(ir_n) * np.exp(-ti / 0.38)
irL = lowpass(irL, 6000)
irR = lowpass(irR, 6000)
irL /= np.sqrt(np.sum(irL ** 2))
irR /= np.sqrt(np.sum(irR ** 2))
revL = signal.fftconvolve(sends.L, irL)[:N]
revR = signal.fftconvolve(sends.R, irR)[:N]

# ---------------------------------------------------------------- mix e master
L = drums.L * 1.0 + bass.L * 1.0 + arp.L + pad.L + fx.L + revL * 0.55
R = drums.R * 1.0 + bass.R * 1.0 + arp.R + pad.R + fx.R + revR * 0.55
L = highpass(L, 30)
R = highpass(R, 30)
# Fade de saída no fim da cauda.
fade = np.ones(N)
f0 = int(14.9 * SR)
fade[f0:] = np.linspace(1, 0, N - f0) ** 1.6
L *= fade
R *= fade
peak = max(np.abs(L).max(), np.abs(R).max())
L /= peak
R /= peak
drive = 1.6
L = np.tanh(L * drive) / np.tanh(drive)
R = np.tanh(R * drive) / np.tanh(drive)
g = 10 ** (-1.0 / 20) / max(np.abs(L).max(), np.abs(R).max())
out = np.stack([L * g, R * g], axis=1)
# Grava nas duas versões do vídeo (site 16:9 e Instagram 9:16), que usam a mesma trilha.
import os
aqui = os.path.dirname(os.path.abspath(__file__))
for pasta in ('site-16x9', 'instagram-9x16'):
    destino = os.path.join(aqui, '..', pasta, 'assets', 'trilha.wav')
    wavfile.write(destino, SR, (out * 32767).astype(np.int16))
    print('gravada', os.path.normpath(destino))
print('pico', np.abs(out).max())
