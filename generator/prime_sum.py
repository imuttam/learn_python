def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_sum_fast(n):
    total = 0
    for start in range(2, n):
        if is_prime(start):
            total += start
    return total


# Get the sum of all primes below 1,000,000
print("The last sum is:", get_prime_sum_fast(1000000))
