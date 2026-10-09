# Servidor estático com UTF-8 e pedidos parciais (Range), para o navegador conseguir buscar pontos dos vídeos.
import os, re, sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class H(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map, '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
                      '.css': 'text/css; charset=utf-8', '.webm': 'video/webm', '.mp4': 'video/mp4', '.json': 'application/json'}
    def log_message(self, *a): pass
    def send_head(self):
        rng = self.headers.get('Range')
        path = self.translate_path(self.path)
        if not rng or os.path.isdir(path) or not os.path.exists(path):
            return super().send_head()
        m = re.match(r'bytes=(\d*)-(\d*)', rng)
        size = os.path.getsize(path)
        a = int(m.group(1)) if m.group(1) else 0
        b = int(m.group(2)) if m.group(2) else size - 1
        b = min(b, size - 1)
        f = open(path, 'rb'); f.seek(a)
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(path))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Range', f'bytes {a}-{b}/{size}')
        self.send_header('Content-Length', str(b - a + 1))
        self.end_headers()
        self._restante = b - a + 1
        return f
    def copyfile(self, src, dst):
        n = getattr(self, '_restante', None)
        if n is None: return super().copyfile(src, dst)
        while n > 0:
            buf = src.read(min(65536, n))
            if not buf: break
            dst.write(buf); n -= len(buf)
    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes'); self.send_header('Cache-Control', 'no-store')
        super().end_headers()

root, port = sys.argv[1], int(sys.argv[2])
ThreadingHTTPServer(('127.0.0.1', port), partial(H, directory=root)).serve_forever()
