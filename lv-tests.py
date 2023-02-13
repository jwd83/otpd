
def liouville_digit(n):
    """Compute the n-th digit of the Liouville constant."""
    factorial = 1
    for i in range(1, n):
        factorial *= i
        if factorial > n:
            break
    return pow(2, factorial, 10)


def liouville_digit_b(n):
    # Calculate the denominator of the n-th term in the sum
    denominator = 1
    for i in range(2, n+1):
        denominator *= i

    # Calculate the n-th decimal digit by taking the n-th digit after the decimal point
    # of the n-th term in the sum
    digit = int(10**n / denominator) % 10

    return digit


for j in range(1, 100000):
    # print j and liouville_digit(j) to the console
    print(j, liouville_digit(j), liouville_digit_b(j))
    # print(j, end=' ')
    # print(liouville_digit(j))
    # print(liouville_digit_b(j))
