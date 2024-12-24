7.def triangle_string_concatenation(n):
    for i in range(1, n + 1):
        line = ' ' * (n - i)
        for x in range(1, 2 * i):
            line += str(x) + ' '
        print(line.strip())  # Strip trailing space
        
# Example usage
triangle_string_concatenation(3)