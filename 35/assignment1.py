1.def factorial_list_comprehension(n):
    return 1 if n == 0 else [i for i in range(1, n + 1)].reduce(lambda x, y: x * y)

# Example usage
print(factorial_list_comprehension(5))  # Output: 120



