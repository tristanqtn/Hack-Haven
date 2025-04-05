```python
import sys

def decrypt_enchanted_cipher(encrypted_text, num_groups, shift_values):
    words = encrypted_text.split()
    alpha_chars = [char for word in words for char in word if char.isalpha()]
    
    decrypted_chars = []
    index = 0
    
    for shift_index in range(num_groups):
        shift = shift_values[shift_index]
        for _ in range(5):
            if index < len(alpha_chars):
                original_char = chr(((ord(alpha_chars[index]) - ord('a') - shift) % 26) + ord('a'))
                decrypted_chars.append(original_char)
                index += 1
    
    # Reconstruct words with spaces
    decrypted_text = ""
    word_index = 0
    for word in words:
        decrypted_text += "".join(decrypted_chars[word_index:word_index + len(word)]) + " "
        word_index += len(word)
    
    return decrypted_text.strip()

# Reading input
input_text = sys.stdin.read().strip().split("\n")
encrypted_text = input_text[0]  # Keep spaces
num_groups = int(input_text[1])
shift_values = list(map(int, input_text[2].strip("[]").split(", ")))

# Decrypt and print the result
print(decrypt_enchanted_cipher(encrypted_text, num_groups, shift_values))

```

`HTB{3NCH4NT3D_C1PH3R_D3C0D3D_b6a8148f3f3417ad9a38bbc62aace376}`