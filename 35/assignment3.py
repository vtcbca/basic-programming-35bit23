3.def fibonacci_generator(max_value):
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b

# Example usage
print(list(fibonacci_generator(50)))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
