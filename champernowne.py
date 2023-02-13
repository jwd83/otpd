import time


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def liouville_digit(n):
    """Compute the n-th digit of the Liouville constant."""
    factorial = 1
    for i in range(1, n):
        factorial *= i
        if factorial > n:
            break
    return pow(2, factorial, 10)


def copeland_erdos_digit(n):
    """Compute the n-th digit of the Copeland-Erdős constant."""
    # Start with the first prime number (2)
    num = 2
    # Keep track of the number of prime digits seen so far
    prime_digits = 0

    # Iterate over all prime numbers and their digits
    while True:
        for digit in str(num):
            if is_prime(prime_digits + 1):
                if prime_digits == n - 1:
                    return int(digit)
                prime_digits += 1
            if prime_digits == n:
                return int(digit)
        num += 1


def champernowne_digit(n, cache={}):
    """
    Compute the n-th digit of the Champernowne constant.

    This version uses caching to speed up later calls.
    """
    # If the desired digit is already in the cache, return it
    if n in cache:
        return cache[n]

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

    # Extract the n-th digit and store it in the cache
    digit = int(str(num)[digit_pos])
    cache[n] = digit

    # Return the n-th digit
    return digit


# Example usage
print(champernowne_digit(1000))  # Output: 3

print(champernowne_digit(1000000))  # Output: 1

start = 272340960540234923409203942093094272340960540234923409203942093094

# time how long this loop takes to execute
start_time = time.time()

loops = 20000
cache = {}
for i in range(1, loops):

    base = start + i * 4
    # sum = champernowne_digit(base) * 1
    # sum += champernowne_digit(base + 1) * 10
    # sum += champernowne_digit(base + 2) * 100
    # sum += champernowne_digit(base + 3) * 1000

    sum = liouville_digit(base) * 1
    sum += liouville_digit(base + 1) * 10
    sum += liouville_digit(base + 2) * 100
    sum += liouville_digit(base + 3) * 1000

    # sum = champernowne_digit(base, cache) * 1
    # sum += champernowne_digit(base + 1, cache) * 10
    # sum += champernowne_digit(base + 2, cache) * 100
    # sum += champernowne_digit(base + 3, cache) * 1000

    # sum = copeland_erdos_digit(base) * 1
    # sum += copeland_erdos_digit(base + 1) * 10
    # sum += copeland_erdos_digit(base + 2) * 100
    # sum += copeland_erdos_digit(base + 3) * 1000

    xor_byte = sum & 0xFF
    # xor_byte = sum % 256
print(xor_byte)
end_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
# display the numbers of loops per second
print("Loops per second: ", end="")
print(loops / (end_time - start_time))
