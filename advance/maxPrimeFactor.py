def isPrime(n):
    r = int(n**0.5+1)
    for i in range(2, r):
        if n % i == 0:
            return False
            break
    return True

lst = set()
def calculate(n):
    for i in range(2, n):
        if n%i == 0 and isPrime(i):
            lst.add(i)
           
    return max(lst)
    
print(calculate(6809))     