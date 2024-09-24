"""write a function to find lcm of given numbers"""

def lcm(n1, n2):
    k = max(n1, n2)

    while True:
        if ( k%n1 ==0 and k%n2 ==0):
            lcm = k
            break
        else:
            k += 1
    return lcm

print(lcm(45, 75))
print(lcm(2, 5))
print(lcm(42,56))