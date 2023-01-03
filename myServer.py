# from http.server import HTTPServer, CGIHTTPRequestHandler

# server_address = ("", 8000)
# httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
# httpd.serve_forever()

import http.server as BaseHTTPServer
import http.server as CGIHTTPServer

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 5000)
handler.cgi_directories = ["/cgi-bin"]

httpd = server(server_address, handler)
httpd.serve_forever()

