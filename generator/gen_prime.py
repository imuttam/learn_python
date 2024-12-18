def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def get_prime(n):
    start = 2
    while start < n:
        if isPrime(start):
            yield start
        start += 1


def get_prime_sum(n):
    total = 0
    start = 2
    while start < n:
        if isPrime(start):
            total += start
            yield total
        start += 1
    

primes = get_prime(200)
for num in primes:
    print(num, end=' ')

print()
sums = get_prime_sum(10000000)
for s in sums:
    last_sum = s

print(last_sum)