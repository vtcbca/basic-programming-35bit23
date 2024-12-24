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