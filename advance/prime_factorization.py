"""
We can break down a composite number into prime factors. For example:
15 = 3 * 5
36 = 2 * 2 * 3 * 3
48 = 2 * 2 * 2 * 2 * 3
Implement a function that takes a natural number as an argument and returns a list containing the prime factorization of that number.
"""
def is_prime(n):
    if n < 2:
        return False

    r = int(n**0.5+1)
    for i in range(2, r):
        if n % i == 0:
            return False
    return True


def check_factor(n):
    result = []
    count = 2
    while count < n:
      
        if (n % count != 0):
            count += 1
        else:
            n = n//2
            result.append(count)
    if n>1:
        result.append(n)
        
    return result

print(check_factor(48))
