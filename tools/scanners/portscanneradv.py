#!/usr/bin/python
import re
import socket
import optparse
import threading
from colorama import Fore, Style


import sys

def is_valid_ipv4(ip):
    # Regular expression for a valid IPv4 address
    ipv4_pattern = re.compile(r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})){3}$')
    return bool(ipv4_pattern.match(ip))

def domain_translate(host):
    if is_valid_ipv4(host):
        return host
    else:
        try:
            ip_address = socket.gethostbyname(host)
            print(f"The IP address of {host} is {ip_address}")
            return(ip_address)
        except socket.error as e:
            print(f"Error resolving {host}: {e}")


def portscanner(IP, port):
    # Convert the port string to an integer
    port = port.strip()
    port = int(port)
    
    # Socket creation for IPV4 and TCP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout to handle non-responsive or closed ports
    sock.settimeout(1)
    # Use connect_ex to check if the port is open or closed
    try:
        sock.connect((IP, port))
        data = sock.recv(1024)
        print(Fore.GREEN + f"Port {port} \topen\t {data.decode('utf-8')}" + Style.RESET_ALL)
    except socket.error as e:
    # If there is an error, print that the port is closed
        print(Fore.RED + f"Port {port} \tclosed" + Style.RESET_ALL)
    except ValueError:
    # If the port string is not a valid integer, print a warning
        print(Fore.YELLOW + f"Invalid port: {port}" + Style.RESET_ALL)
    # Socket closure
    sock.close()



def portScan(host, ports):
    target = domain_translate(host)
    threads = []
    for port in ports:
        thread = threading.Thread(target=portscanner, args=(target,port,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


def main():
    parser = optparse.OptionParser()

    # Add options for host and port
    parser.add_option('-H', dest='host', type='string', help='Specify target host')
    parser.add_option('-p', dest='ports', type='string', help='Specify target port(s), separated by commas')

    # Parse command line arguments
    (options, args) = parser.parse_args()

    # Check if both host and port options are provided
    if not options.host or not options.ports:
        print("Both host and port options are required. Use -h or --help for more information.")
        sys.exit(0)

    # Split ports into a list
    ports = options.ports.split(',')

    # Display information
    print(f"Target Host: {options.host}")
    print(f"Target Port(s): {', '.join(ports)}")

    # Run portScan function
    portScan(options.host, ports)

if __name__ == "__main__":
    main()

# python script_name.py -H 127.0.0.1 -p 80,443,22
