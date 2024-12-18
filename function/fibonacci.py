"""program to display  fibonacci series."""

def fib(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(20):
    print(fib(i), end=' ')