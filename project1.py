import socket

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for connection attempts
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except socket.error as e:
        print(f"Error scanning port {port}: {e}")

target_ip = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"Scanning target: {target_ip} from port {start_port} to {end_port}")
for port in range(start_port, end_port + 1):
    scan_port(target_ip, port)