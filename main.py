import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv


load_dotenv()

PORT = int(os.environ.get('PORT'))
REDIRECT_URL = os.environ.get('REDIRECT_URL')


class Redirect(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location', REDIRECT_URL)
        self.end_headers()


HTTPServer(("", PORT), Redirect).serve_forever()
