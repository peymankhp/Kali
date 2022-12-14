import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# here we asking for the target website
# Ask for start port and end port
target = input('Please type IP: ')
port_start = input('Scan port from?  ')
port_end = input('Scan port to?  ')

# next line gives us the ip address
# of the target
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

# function for scanning ports
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False
start = time.time()

for port in range(int(port_start),int(port_end)):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')

end = time.time()
print(f'Time taken {end - start:.2f} seconds')