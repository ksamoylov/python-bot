import http.server
import ast
import json
from src.bot.services.bot_service import handle_hook_event
from http import HTTPStatus


class RequestHandler(http.server.BaseHTTPRequestHandler):
    PORT: int = 80
    HOST: str = 'localhost'

    def do_GET(self) -> None:
        self.send_response(self)

    def do_POST(self) -> None:
        self.set_response()
        content_length = int(self.headers['Content-Length'])
        post = self.rfile.read(content_length).decode('utf-8')

        post_data = json.loads(post)
        handle_hook_event(post_data)

    def set_response(self) -> None:
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
