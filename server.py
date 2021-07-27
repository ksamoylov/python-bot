from http.server import HTTPServer
from src.http.handlers.RequestHandler import RequestHandler


def run():
    try:
        port = RequestHandler.PORT
        server = HTTPServer(('', port), RequestHandler)
        print(f"Server is running on {RequestHandler.HOST}:{port}")
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()


if __name__ == "__main__":
    run()
