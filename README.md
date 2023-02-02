# Clickjacker

## Usage
```
Usage:
	python3 clickjack.py -t <target> [--PoC | -lh <local_host> | -lp <local_port>]

Flags:
	-t,    Set target to create a website that hijacks clicks on it.
	--PoC, Run proof of concept.
	-lh,   Set the host where the web server is going to be running (default: localhost). { Not Implemented }
	-lp,   Set the port where the web server is going to be running (default: 8000).      { Not Implemented }
```

Run proof of concept:
```
python3 clickjack.py --PoC -t http://example.com
```

Run a clickjacking web server to attack: **{ Not Implemented }**
```
python3 clickjack.py -t http://example.com -lh example.io -lp 443
```

## Manual Usage
Edit the PoC.html file, where it says "`<target>`", change it to the target you want to emulate. You also need to create the text fields & buttons, and adjust them to the website you are emulating.
Then run this command:
```
python3 -m http.server <port>
```
