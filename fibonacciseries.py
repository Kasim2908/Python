def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
n = 10  # Number of terms in the Fibonacci sequence
fib_sequence = fibonacci(n)
print(f"First {n} terms of the Fibonacci sequence: {fib_sequence}")
