import itertools
from concurrent.futures import ThreadPoolExecutor

encrypted_flag = "C_ef8K8rT83JC8I0fOPiN6P!liE03W2NXFh1viJCROAqXb6o"
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"
n = len(charset)

def mod_inverse(a, n):
    t, newt = 0, 1
    r, newr = n, a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return None  # No inverse if a and n are not coprime
    if t < 0:
        t += n
    return t

def inverse_permute(permuted_message):
    p = [4, 3, 0, 5, 1, 2, 10, 9, 6, 11, 7, 8, 16, 15, 12, 17, 13, 14, 22, 21, 18, 23, 19, 20, 28, 27, 24, 29, 25, 26, 34, 33, 30, 35, 31, 32, 40, 39, 36, 41, 37, 38, 46, 45, 42, 47, 43, 44]
    inverse_p = [0] * len(p)
    for index, value in enumerate(p):
        inverse_p[value] = index
    return ''.join(permuted_message[i] for i in inverse_p)

def inverse_round(encrypted_message, A, B, n):
    permuted = inverse_permute(encrypted_message)
    decrypted = ""
    for i in range(len(permuted)):
        y = charset.index(permuted[i])
        a = A[i % 6]
        b = B[i % 6]
        a_inv = mod_inverse(a, n)
        if a_inv is None:
            raise ValueError("No modular inverse exists for a = {} with n = {}".format(a, n))
        decrypted += charset[(a_inv * (y - b)) % n]
    return decrypted

def decrypt_round(args):
    encrypted, A, B, num_rounds = args
    decrypted = encrypted
    for round_index in range(num_rounds):
        current_A = A[round_index * 6:(round_index + 1) * 6]
        current_B = B[round_index * 6:(round_index + 1) * 6]
        decrypted = inverse_round(decrypted, current_A, current_B, n)
    if decrypted.startswith("404CTF{tHe_c"):
        print(f"Decrypted: {decrypted}")
        print(f"Rounds: {num_rounds}, A: {A}, B: {B}")
        return decrypted

def decrypt(encrypted):
    results = []
    with ThreadPoolExecutor() as executor:
        futures = []
        for num_rounds in range(1, 7):
            A_range = itertools.product(range(2, n), repeat=6 * num_rounds)
            B_range = itertools.product(range(1, n), repeat=6 * num_rounds)
            for A in A_range:
                for B in B_range:
                    args = (encrypted, A, B, num_rounds)
                    future = executor.submit(decrypt_round, args)
                    futures.append(future)
        for future in futures:
            result = future.result()
            if result:
                results.append(result)
    return results

if __name__ == "__main__":
    decrypted_flags = decrypt(encrypted_flag)
    for flag in decrypted_flags:
        print(flag)
