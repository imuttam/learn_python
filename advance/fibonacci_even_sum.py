"""Find the sum of all even elements of the Fibonacci sequence with values less than 1,000,000 (1 million)."""

def calculate():
    total = 0
    a = 0
    b = 1
    while a < 1000000:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total


print(calculate())