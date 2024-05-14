import random as rd

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"

def f(a,b,n,x):
	return (a*x+b)%n

def f_inverse(a, b, n, y):
    # Find the modular multiplicative inverse of a modulo n
    a_inv = pow(a, -1, n)  # Using pow function to find the modular inverse
    return (a_inv * (y - b)) % n

def encrypt(message,a,b,n):
	encrypted = ""
	for char in message:
		x = charset.index(char)
		x = f(a,b,n,x)
		encrypted += charset[x]
	return encrypted


def decrypt(encrypted, a, b, n):
    decrypted = ""
    for char in encrypted:
        y = charset.index(char)
        x = f_inverse(a, b, n, y)
        decrypted += charset[x]
    return decrypted

n = len(charset)
for a in range (2,n):
	for b in range (1,n):
		# if the output of decrypt("-4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_",a,b,n) starts with "404CTF{", then print the flag
		output = decrypt("-4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_",a,b,n)
		if output.startswith("404CTF{"):
			print("ENCRYPTED FLAG : -4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_")
			print("a = ",a)
			print("b = ",b)
			print(output)
			exit()
# ENCRYPTED FLAG : -4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_