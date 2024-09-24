"""write a program to find factor of a number"""

def factor(num):
    lst = []

    for i in range(1, num//2):
        if num%i == 0:
            lst.append(i)
    lst.append(num)
    return lst

print(factor(24))

