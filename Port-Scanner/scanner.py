import socket
import argparse
import time
open_ports=0

def scan_port(host,port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        return sock.connect_ex((host,port))

parser = argparse.ArgumentParser(description="Simple TCP port scanner")
parser.add_argument("Host", help="target hostname or IP address")
parser.add_argument("--start", type=int, default=1, help="Starting port")
parser.add_argument("--end", type = int, default=100, help="Ending Port")
args = parser.parse_args()
try:
    host = socket.gethostbyname(args.Host)
except socket.gaierror:
    print(f"Could not resolve host: {args.Host}")
    exit()
if not (1 <= args.start <= 65535):
    print("Start port must be between 1 and 65535.")
    exit()
if not (1 <= args.end <= 65535):
    print("End port must be between 1 and 65335.")
    exit()
if args.start> args.end:
    print("Start port cannot be bigger than end port.")
    exit()

print(f"Scanning {args.Host} ({host}) from port {args.start} to {args.end} ")
start_time = time.perf_counter()
for port in range(args.start, args.end+1):
    result=scan_port(host,port)

    if result == 0:
        print(f"Port {port} is open.")
        open_ports+=1
elapsed = time.perf_counter() - start_time
    
print(f"Scan completed in {elapsed:.2f} seconds")
print(f"Number of open ports found: {open_ports}")




