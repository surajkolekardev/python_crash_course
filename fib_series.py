# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example: Generate Fibonacci series of 10 terms
n_terms = 10
fib_series = fibonacci(n_terms)
print(f"Fibonacci series with {n_terms} terms: {fib_series}")
