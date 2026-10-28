import unittest
from http.client import HTTPConnection
from threading import Thread
from http.server import ThreadingHTTPServer

from app import AppHandler


class AppRoutesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), AppHandler)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def get(self, path):
        connection = HTTPConnection("127.0.0.1", self.port, timeout=3)
        connection.request("GET", path)
        response = connection.getresponse()
        body = response.read()
        headers = dict(response.getheaders())
        connection.close()
        return response.status, headers, body

    def test_registered_routes(self):
        routes = {
            "/": "text/html",
            "/calculations": "text/html",
            "/advanced-calculations.html": "text/html",
            "/style.css": "text/css",
            "/images/apple.svg": "image/svg+xml",
            "/images/banana.svg": "image/svg+xml",
            "/images/orange.svg": "image/svg+xml",
            "/images/grapes.svg": "image/svg+xml",
            "/images/strawberry.svg": "image/svg+xml",
        }
        for path, content_type in routes.items():
            with self.subTest(path=path):
                status, headers, body = self.get(path)
                self.assertEqual(status, 200)
                self.assertTrue(headers["Content-Type"].startswith(content_type))
                self.assertGreater(len(body), 0)
                self.assertEqual(headers["X-Content-Type-Options"], "nosniff")

    def test_calculations_alias_accepts_query_string(self):
        status, _, body = self.get("/calculations?from=home")
        self.assertEqual(status, 200)
        self.assertIn(b"Scientific calculator", body)

    def test_unregistered_and_traversal_paths_return_404(self):
        for path in ("/missing", "/README.md", "/images/../README.md"):
            with self.subTest(path=path):
                status, _, _ = self.get(path)
                self.assertEqual(status, 404)


if __name__ == "__main__":
    unittest.main()