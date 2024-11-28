
a,b = 0,1
for i in range(10):
    print(a, end=" ")
    a,b = b, a+b 

def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print()
for i in range(10):
    print(fib(i), end=' ')
