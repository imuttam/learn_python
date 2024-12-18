"""write a function which takes two parameter and if both are even return lesser one else return odd number"""

def lesser_even(a,b):
    if a%2 == 0 and b%2 ==0:
        return min(a,b)
    elif a%2 != 0:
        return a
    elif b%2 != 0:
        return b

print(lesser_even(2,4))
print(lesser_even(2,5))
print(lesser_even(3,5))

