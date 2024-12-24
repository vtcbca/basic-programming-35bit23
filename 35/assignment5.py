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