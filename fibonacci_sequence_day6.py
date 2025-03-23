def fibonacci_sequence(n):
    """Generate a Fibonacci sequence up to the nth number."""
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

user_input_sequence = int(input("Enter an integer to find its Fibonacci sequence: "))
print(f"Fibonacci sequence: {fibonacci_sequence(user_input_sequence)}")
