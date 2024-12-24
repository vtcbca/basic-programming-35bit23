solution

1.def factorial_list_comprehension(n):
    return 1 if n == 0 else [i for i in range(1, n + 1)].reduce(lambda x, y: x * y)

# Example usage
print(factorial_list_comprehension(5))  # Output: 120


2.def is_prime_list_comprehension(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, n))

# Example usage
print(is_prime_list_comprehension(11))  # Output: True
print(is_prime_list_comprehension(15))  # Output: False


3.def fibonacci_generator(max_value):
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b

# Example usage
print(list(fibonacci_generator(50)))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


4.def reverse_string_stack(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()  # Pop the last character
    return reversed_str

# Example usage
print(reverse_string_stack("hello"))  # Output: "olleh"


5.def is_palindrome_stack(s):
    s = s.lower().replace(" ", "")  # Ignore spaces and case
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()  # Pop characters from stack
    return s == reversed_str

# Example usage
print(is_palindrome_stack("A man a plan a canal Panama"))  # Output: True
print(is_palindrome_stack("hello"))  # Output: False


6.def pattern_string_concatenation(n):
    for i in range(1, n + 1):
        line = ''
        for j in range(i):
            line += '* '
        print(line.strip())  # Strip the trailing space

# Example usage
pattern_string_concatenation(4)

7.def triangle_string_concatenation(n):
    for i in range(1, n + 1):
        line = ' ' * (n - i)
        for x in range(1, 2 * i):
            line += str(x) + ' '
        print(line.strip())  # Strip trailing space
        
# Example usage
triangle_string_concatenation(3)

8.def alphabet_pattern_string_concatenation(n):
    for i in range(1, n + 1):
        # Calculate spaces for the current row
        spaces = ' ' * (n - i) * 2
        
        # Create the alphabet sequence
        forward_seq = ''.join([chr(65 + j) for j in range(i)])  # A, B, C, ...
        backward_seq = forward_seq[:-1][::-1]  # A, B, ... and then reversed
        
        # Combine forward and backward sequence with spaces
        row = '   '.join(forward_seq + backward_seq)
        
        # Print the row with spaces
        print(spaces + row)

# Example usage
alphabet_pattern_string_concatenation(3)
