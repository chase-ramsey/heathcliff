import json
from http.server import CGIHTTPRequestHandler, HTTPServer


class Server(CGIHTTPRequestHandler):
    def do_GET(self):
        if False:
            self.send_response_only(404, 'Not found')
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.get_messages()

    def do_POST(self):
        if False:
            self.send_response_only(404, 'Not found')
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.write_message()

    def get_messages(self):
        with open('test.txt', 'r') as f:
            messages = []
            for msg in f.read().split('\n'):
                if msg:
                    messages.append(msg)

            self.wfile.write(json.dumps({'messages': messages}).encode('utf-8'))

    def write_message(self):
        data = ''
        buf = self.request.recv(2048)
        while buf:
            data += buf.decode('utf-8')
            buf = self.request.recv(2048)

        with open('test.txt', 'a') as f:
            if data:
                f.write('{}\n'.format(data))



def run(server_class=HTTPServer, handler_class=Server):
    server_address = ('', 5000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    try:
        run()
    except (Exception, KeyboardInterrupt) as ex:
        print(ex)
