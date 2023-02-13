
def champernowne_digit(n):
    """Compute the n-th digit of the Champernowne constant."""
    # Compute the number of digits in the block of numbers containing n
    digits_per_block = 1
    while True:
        num_blocks = 10 ** digits_per_block - 10 ** (digits_per_block - 1)
        if n <= num_blocks * digits_per_block:
            break
        n -= num_blocks * digits_per_block
        digits_per_block += 1

    # Compute the number containing the n-th digit
    num = 10 ** (digits_per_block - 1) + (n - 1) // digits_per_block

    # Compute the position of the n-th digit within the number
    digit_pos = (n - 1) % digits_per_block

    # Extract and return the n-th digit
    return int(str(num)[digit_pos])


# Example usage
print(champernowne_digit(1000))
