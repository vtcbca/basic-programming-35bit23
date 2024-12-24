2.def is_prime_list_comprehension(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, n))

# Example usage
print(is_prime_list_comprehension(11))  # Output: True
print(is_prime_list_comprehension(15))  # Output: False