from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import json

def logPathTime(c):
        f = open('log.txt', 'a')
        f.write("Path: %s; Time: %s \n" % (c.path, BaseHTTPRequestHandler.date_time_string(c)))
        return

def logMessageJSON(message):
        with open('messages.json', mode='r', encoding='utf-8') as feedsjson:
            feeds = json.load(feedsjson)
        with open('messages.json', mode='w', encoding='utf-8') as f:
            f = json.dump([], f)
        with open('messages.json', mode='w', encoding='utf-8') as feedsjson:
            entry = {"message": message}
            feeds.append(entry)
            json.dump(feeds, feedsjson)

def logMessage(message):
    nmes1 = message.replace("['", "")
    nmes = nmes1.replace("']", "")
    f = open('messages.txt', 'a')
    f.write(nmes + "\n")
    f.close()
    return

class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
                query = parse_qs(urlparse(self.path).query)
                if self.path.startswith("/messages"):
                        self.send_response(200)
                        self.send_header('Access-Control-Allow-Origin','*')
                        self.end_headers()
                        with open('messages.json') as data_file:
                            data = json.load(data_file)
                        print(data)
                        sdata = str.encode(json.dumps(data))
                        print(sdata)
                        self.wfile.write(bytes(sdata))
                        logPathTime(self)
                else:
                        self.send_response(404)
                        self.send_header('Access-Control-Allow-Origin','*')
                        self.end_headers()
                        self.wfile.write(bytes("Page not found. 404", "utf-8"))
                        logPathTime(self)
                return

        def do_POST(self):
                if self.path.startswith("/messages"):
                        self.send_response(201)
                        self.send_header('Access-Control-Allow-Origin','*')
                        self.end_headers()
                        length = int(self.headers['Content-Length'])
                        data = self.rfile.read(length).decode("utf-8")
                        parsed_data = parse_qs(data)
                        print(parsed_data)
                        print(data)
                        strdata = str(parsed_data)
                        logMessageJSON(data)
                else:
                        self.send_response(404)
                        self.end_headers()
                        self.wfile.write(bytes("404", "utf-8"))
                        return

def run():
        listen = ('127.0.0.1', 8080)
        server = HTTPServer(listen,MyServer)
        print ("Listening...")
        server.serve_forever()

run()
