def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibs = [0, 1]
        for i in range(2, n + 1):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs[n]

def gen():
    a = 0
    total = 0
    while True:
        term = fib(a)
        if term >= 1000000:
            break
        if term % 2 == 0:
            total += term
            yield total
        a += 1

g = gen()

# Print some results
for _ in range(20):  # Example: print the first 10 terms
    try:
        print(next(g))
    except StopIteration:
        break

# for i in range(10):
#     print(fib(i))