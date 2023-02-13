# otpd

## one-time-pad-disjunctive

A likely horribly insecure encryption algorithm based on ideas I had a long time
ago about using digits from pi as a source of bits for a one time pad-like
encryption algorithm. The key is the starting position in the digits.

When I tried to implement it, I realized that the digits of pi are incredibly
slow to calculate to an arbitrary location and looked for other sources of
arbitrary digits and stumbled across the field of disjunctive numbers. After
some research it appeared the best number to use was the Liouville number.

The key used to encrypt and decrypt sample txt and png files is: 234234234234
