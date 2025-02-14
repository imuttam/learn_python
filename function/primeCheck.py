def displayPrime(n):
    for i in range(2,n):
        if not isPrime(i):
            continue
        else:
            print(f"{i} is Prime Number.")            

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
            
            
displayPrime(1000)
    