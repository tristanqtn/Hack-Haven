import itertools
encrypted_flag = "C_ef8K8rT83JC8I0fOPiN6P!liE03W2NXFh1viJCROAqXb6o"

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"
n = len(charset)

def mod_inverse(a, n):
    # This function returns the modular inverse of a under modulo n
    # Use the extended Euclidean algorithm to find the inverse
    t, newt = 0, 1
    r, newr = n, a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return None  # No inverse if a and n are not coprime
    if t < 0:
        t = t + n
    return t

def g(a, b, n, y):
    a_inv = mod_inverse(a, n)
    if a_inv is None:
        raise ValueError("No modular inverse exists, the function is not reversible for these parameters")
    x = (a_inv * (y - b)) % n
    return x

def inverse_permute(permuted_message):
    # This is the permutation used in the original permute function
    p = [4, 3, 0, 5, 1, 2, 10, 9, 6, 11, 7, 8, 16, 15, 12, 17, 13, 14, 22, 21, 18, 23, 19, 20, 28, 27, 24, 29, 25, 26, 34, 33, 30, 35, 31, 32, 40, 39, 36, 41, 37, 38, 46, 45, 42, 47, 43, 44]
    # Create an empty list to store the inverse permutation
    inverse_p = [0] * len(p)
    
    # Compute the inverse permutation indices
    for index, value in enumerate(p):
        inverse_p[value] = index
    
    # Use the inverse permutation indices to reorder the message back to its original order
    original_message = [''] * len(permuted_message)
    for i in range(len(permuted_message)):
        original_message[inverse_p[i]] = permuted_message[i]
    
    return ''.join(original_message)

def inverse_round(encrypted_message, A, B, n):
    # First, unpermute the message
    permuted = inverse_permute(encrypted_message)
    decrypted = ""
    
    for i in range(len(permuted)):
        y = charset.index(permuted[i])
        a = A[i % 6]
        b = B[i % 6]
        a_inv = mod_inverse(a, n)
        if a_inv is None:
            raise ValueError("No modular inverse exists for a = {} with n = {}".format(a, n))
        x = (a_inv * (y - b)) % n
        decrypted += charset[x]
    
    return decrypted

def decrypt(encrypted):
    for num_rounds in range(1, 7):
        for A in itertools.product(range(2, n), repeat=6 * num_rounds):
            for B in itertools.product(range(1, n), repeat=6 * num_rounds):
                decrypted = encrypted
                for round_index in range(num_rounds):
                    current_A = A[round_index * 6:(round_index + 1) * 6]
                    current_B = B[round_index * 6:(round_index + 1) * 6]
                    decrypted = inverse_round(decrypted, current_A, current_B, n)
                print(decrypted)
                if decrypted.startswith("404CTF{"):
                    print(f"Decrypted: {decrypted}")
                    print(f"Rounds: {num_rounds}, A: {A}, B: {B}")
                    return decrypted
                
decrypt(encrypted_flag)
