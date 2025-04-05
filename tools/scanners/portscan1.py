#!/usr/bin/python

import socket
from colorama import Fore, Style

def portscanner(IP, port):
    # Socket creation for IPV4 and TCP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout to handle non-responsive or closed ports
    sock.settimeout(2);
    # Use connect_ex to check if the port is open or closed
    result = sock.connect_ex((IP, port))
    # Check the result of the connection attempt
    if result == 0:
        message = Fore.GREEN + f"Port {port} open" + Style.RESET_ALL
    else:
        message = Fore.RED + f"Port {port} closed" + Style.RESET_ALL
    # Socket closure
    sock.close()

    return message

target_IP = "10.0.2.4"
target_port = 445
port_limit = 1024

print(f"ONE PORT {target_port}")
result_message = portscanner(target_IP, target_port)
print(result_message)


print(f"\n\nSCANNING ALL FIRST {port_limit} PORTS")
for port in range(0, port_limit+1):
	result_message = portscanner(target_IP, port)
	print(result_message)
