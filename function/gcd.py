"""write a function to find gcd of a number"""

def gcd(n1, n2):
    k = min(n1, n2)

    while True:
        if (n1% k ==0 and n2%k ==0):
            gcd = k
            break
        else:
            k -= 1
    return gcd

print(gcd(45, 75))
print(gcd(2, 5))
print(gcd(42,56))