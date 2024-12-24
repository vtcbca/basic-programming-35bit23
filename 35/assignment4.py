4.def reverse_string_stack(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()  # Pop the last character
    return reversed_str

# Example usage
print(reverse_string_stack("hello"))  # Output: "olleh"
