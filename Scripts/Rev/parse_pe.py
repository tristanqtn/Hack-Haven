import sys
from pefile import PE

def parse_pe(file_path):
    pe = PE(file_path)
    print("PE Sections:")
    for section in pe.sections:
        print(f"[{section.Name.decode().strip()}] Virtual Address: {hex(section.VirtualAddress)}, Size: {section.SizeOfRawData}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <pe_file>")
        sys.exit(1)
    parse_pe(sys.argv[1])
