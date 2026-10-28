from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


HOST = "127.0.0.1"
PORT = 8000
ROOT = Path(__file__).resolve().parent
ROUTES = {
    "/": "index.html",
    "/calculations": "advanced-calculations.html",
    "/advanced-calculations.html": "advanced-calculations.html",
    "/style.css": "style.css",
    "/images/apple.svg": "images/apple.svg",
    "/images/banana.svg": "images/banana.svg",
    "/images/orange.svg": "images/orange.svg",
    "/images/grapes.svg": "images/grapes.svg",
    "/images/strawberry.svg": "images/strawberry.svg",
}


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlsplit(self.path).path
        relative_path = ROUTES.get(route)
        if relative_path is None:
            self.send_error(404, "Not found")
            return

        file_path = ROOT / relative_path
        try:
            content = file_path.read_bytes()
        except OSError:
            self.send_error(404, "Not found")
            return

        content_type = {
            ".html": "text/html; charset=utf-8",
            ".css": "text/css; charset=utf-8",
            ".svg": "image/svg+xml; charset=utf-8",
        }.get(file_path.suffix, "application/octet-stream")
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(content)


def main():
    server = ThreadingHTTPServer((HOST, PORT), AppHandler)
    print(f"Hello World is running at http://{HOST}:{PORT}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()