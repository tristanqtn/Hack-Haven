# Encryption code : 

```python
import random as rd

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"

def f(a,b,n,x):
	return (a*x+b)%n

def encrypt(message,a,b,n):
	encrypted = ""
	for char in message:
		x = charset.index(char)
		x = f(a,b,n,x)
		encrypted += charset[x]

	return encrypted

n = len(charset)
a = rd.randint(2,n-1)
b = rd.randint(1,n-1)

print(encrypt(FLAG,a,b,n))

# ENCRYPTED FLAG : ZnBsgvWYhC5bw{xR5sbwvCnbs5XhXpbI9SL
```

# Decryption code : 

```python
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"

def modinv(a, n):
    """Find the modular inverse of a modulo n using the extended Euclidean algorithm."""
    t, newt = 0, 1
    r, newr = n, a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return None  # No modular inverse
    if t < 0:
        t = t + n
    return t

def decrypt(encrypted_message, a, b, n):
    decrypted = ""
    a_inv = modinv(a, n)
    if a_inv is None:
        raise ValueError("No modular inverse found for a!")
    
    for char in encrypted_message:
        x_prime = charset.index(char)
        x = (a_inv * (x_prime - b)) % n
        decrypted += charset[x]

    return decrypted

# Encrypted flag
encrypted_flag = "ZnBsgvWYhC5bw{xR5sbwvCnbs5XhXpbI9SL"

# Charset length
n = len(charset)

# Brute-force through possible values of a and b
for a in range(2, n):
    a_inv = modinv(a, n)
    if a_inv is not None:  # Check if a has an inverse
        for b in range(1, n):
            try:
                decrypted_flag = decrypt(encrypted_flag, a, b, n)
                if "Star{" in decrypted_flag :
                    print(f"Decrypted flag: {decrypted_flag}")
                    print(f"Found with a = {a}, b = {b}")
                    break
            except Exception as e:
                pass

```