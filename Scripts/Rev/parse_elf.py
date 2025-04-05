import sys
from elftools.elf.elffile import ELFFile

def parse_elf(file_path):
    with open(file_path, 'rb') as f:
        elf = ELFFile(f)
        print("ELF Sections:")
        for section in elf.iter_sections():
            print(f"[{section.name}] Offset: {section['sh_offset']}, Size: {section['sh_size']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <elf_file>")
        sys.exit(1)
    parse_elf(sys.argv[1])
