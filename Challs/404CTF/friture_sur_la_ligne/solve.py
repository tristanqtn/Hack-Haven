import numpy as np

def read_channel_data(channel):
    with open(f"channel_{channel}", "r") as f:
        data = f.read().strip()
    return np.array([int(bit) for bit in data], dtype='uint8')

def reconstruct_and_correct(data_channels):
    n = len(data_channels[0])
    reconstructed = np.zeros(n * 8, dtype='uint8')
    for i in range(8):
        reconstructed[i::8] = data_channels[i]
    return reconstructed

def decode_and_correct_errors(encoded_bits):
    decoded_bits = []
    for i in range(0, len(encoded_bits), 8):
        byte = encoded_bits[i:i+7]
        parity = encoded_bits[i+7]
        if sum(byte) % 2 != parity:
            # Assuming error is in the bit from channel 4 (index 3 in the byte)
            byte[3] = 1 - byte[3]  # Flip the bit
            # Recalculate parity after flipping
            if sum(byte) % 2 != parity:
                # If still wrong, revert the flip (indicating error might be elsewhere)
                byte[3] = 1 - byte[3]
        decoded_bits.extend(byte)
    return np.packbits(decoded_bits)

def reconstruct_image(decoded_bytes):
    with open("reconstructed_flag.png", "wb") as img_file:
        img_file.write(decoded_bytes.tobytes())

# Main execution
data_channels = [read_channel_data(i) for i in range(1, 9)]
reconstructed_bits = reconstruct_and_correct(data_channels)
original_bytes = decode_and_correct_errors(reconstructed_bits)
reconstruct_image(original_bytes)
