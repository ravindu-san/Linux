import http.server
import socketserver

PORT=8081

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",PORT), Handler)

print("File Server Running @ PORT ", PORT)

httpd.serve_forever()
