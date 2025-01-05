This challenge learns you how to use pwntools (python lib) to automate a TCP communication. In the end pwntools is used in the PWN categ to exploit some applicative vulns. 

```python
from pwn import *

# Define the host and port
host = "challenges.hackademint.org"
port = 32450

# Connect to the remote service
conn = remote(host, port)

# Receive the initial message and wait for "Saisissez OK pour continuer"
conn.recvuntil(b"Saisissez OK pour continuer >")

# Send "OK" to continue
conn.sendline(b"OK")

# Read the next message (prompting for Fibonacci numbers)
conn.recvuntil(b">")

# Function to compute the Fibonacci sequence
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Get the first 30 Fibonacci numbers
fib_seq = fibonacci(30)

# Send each Fibonacci number one by one
for num in fib_seq:
    conn.sendline(str(num).encode())  # Send each number as a string
# Wait for the final prompt with a number
final_prompt = conn.recvuntil(b"Voici un nombre : ")
number = conn.recvline().strip().decode()  # Read the number

# Print the number (for verification)
print("Received number:", number)

# Send the number back to the server
conn.sendline(number.encode())

# (Optional) - Read the final response from the server
response = conn.recvall(timeout=2)
print(response.decode())

# Close the connection
conn.close()
```