"""Implement a function called is_prime() that takes a natural number as an argument and checks if it is a prime number.
     In the case of a prime number, the function returns True, otherwise False."""


def is_prime(n):
    if n < 2:
        return False

    r = int(n**0.5+1)
    for i in range(2, r):
        if n % i == 0:
            return False

    return True

print(is_prime(11))
print(is_prime(100271))