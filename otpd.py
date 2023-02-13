
import sys

# look at optimizing this function. we can return the i and factorial to the caller
# and have them supply these to more efficiently compute the next liouville digit


def liouville_digit(n):
    """Compute the n-th digit of the Liouville constant."""
    factorial = 1
    for i in range(1, n):
        factorial *= i
        if factorial > n:
            break
    return pow(2, factorial, 10)


# get the filename from the command line
filename = sys.argv[1]

# get the starting position of the liouville digit from the command line
seed = int(sys.argv[2])

# check if the file is type otpd
if filename.endswith('.otpd'):
    output_filename = filename[:-5]
else:
    output_filename = filename + '.otpd'

# open the input file to read in a byte at a time
with open(filename, 'rb') as input_file:
    # open the output file to write in a byte at a time
    with open(output_filename, 'wb') as output_file:
        # read in a byte from the input file
        byte = input_file.read(1)

        # while there are still bytes to read
        while byte:
            # grab the next 3 liouville digits and convert them to an integer
            liouville = int(
                ''.join([str(liouville_digit(seed + i)) for i in range(3)]))

            # store the low byte of the liouville digit
            low_byte = liouville & 0xFF

            # xor the low byte of the liouville digit with the byte from the input file
            output_byte = low_byte ^ ord(byte)

            # convert an int to a byte
            output_byte = bytes([output_byte])

            # write the output byte to the output file
            output_file.write(output_byte)

            # read in the next byte from the input file
            byte = input_file.read(1)

            # increment the seed
            seed += 3
