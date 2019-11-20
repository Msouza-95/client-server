import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Disponivel na Porta ", PORT)
    httpd.serve_forever()
    #pagina de apoio
    # https://docs.python.org/3/library/http.server.html#module-http.server