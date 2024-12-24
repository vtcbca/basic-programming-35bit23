6.def pattern_string_concatenation(n):
    for i in range(1, n + 1):
        line = ''
        for j in range(i):
            line += '* '
        print(line.strip())  # Strip the trailing space

# Example usage
pattern_string_concatenation(4)