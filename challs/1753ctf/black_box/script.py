def decode(encoded_message):
    # Convert the encoded message into a list of bytes for easy manipulation
    message_bytes = list(encoded_message)

    # Define the swaps in reverse order to decode
    swaps = [(19, 11), (18, 10), (14, 8), (12, 7), (6, 9), (3, 4), (2, 17), (1, 5), (0, 16)]

    # Perform the byte swaps
    for a, b in swaps:
        message_bytes[a], message_bytes[b] = message_bytes[b], message_bytes[a]

    # Convert the list of bytes back into a string
    decoded_message = ''.join(message_bytes)
    return decoded_message

# Encoded message
encoded_message = "3{Lc374_0LU}UMKD155Z"

# Decode the message
decoded_message = decode(encoded_message)
print("Decoded message:", decoded_message)