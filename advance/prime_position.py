"""Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, ...
   The prime number in position one is 2. The prime number in position two is 3. The prime number in position three is 5.
   Implement a function that returns a prime number at position 100."""


def is_prime(n):
    if n < 2:
        return False

    r = int(n**0.5+1)
    for i in range(2, r):
        if n % i == 0:
            return False

    return True

# count = 0

# while count <5:


