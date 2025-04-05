from myhdl import Signal, modbv

# Constants
A = 7
B = 1918273
N = 25

# Data from checker
data = [
    78, 114, 87, 9, 245, 67, 252, 90, 90, 126,
    120, 109, 133, 78, 206, 121, 52, 115, 123,
    102, 164, 194, 170, 123, 5,
]

def simulate_state(initial_state):
    # Initialize the state
    state = initial_state
    states = []
    for _ in range(N):
        state = (A * state + B) % 256
        states.append(state)
    return states

# Testing with a range of initial states
for initial in range(256):
    states = simulate_state(initial)
    password_chars = []
    for i in range(N):
        # Perform XOR and keep within printable ASCII range
        ascii_val = data[i] ^ states[i]
        if 32 <= ascii_val <= 126:
            char = chr(ascii_val)
        else:
            char = '.'  # Replace non-printable characters with a dot
        password_chars.append(char)
    password = ''.join(password_chars)
    print(f"Initial state {initial}: Password recovered = {password}")
