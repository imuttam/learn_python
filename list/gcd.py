"""Implement a function called greatest_common_divisor() that determines the greatest common divisor of two numbers."""


def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
        print(a,b)
    return a


print(greatest_common_divisor(24, 36))
print(greatest_common_divisor(5, 48))