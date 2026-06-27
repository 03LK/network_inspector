import socket
import subprocess
import requests

def dns_resolve(host):
    try:
        print(socket.gethostbyname(host))
    except:
        print("this domain is not exist")
        return 25

def ping_checker(host):
    result = subprocess.run(["ping", host, "-n", "2"], encoding="cp866", capture_output=True, text=True)
    print(result.stdout)

def port_scanner(host):
    ports=[53, 80, 443]
    for p in ports:
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex((host, p))
        s.close()
        if result == 0:
            print("port ", p, "OPEN")
        else:
            print("port ", p, "CLOSED")

def http_insp(host):
    r = requests.get("https://" + host)
    print(r.url, "\n", r.status_code, "\n", r.headers.get("Server", "NOPE"), "\n", r.headers.get("Content-Type", "NOPE"))

def inspector():
    while True:
        host = input("domain: ")
        if host=="X":
            break
        if dns_resolve(host)==25:
            continue
        ping_checker(host)
        port_scanner(host)
        http_insp(host)
        print("\n#################\nFor exit press X\n#################\n")
    
inspector()
