"""Implement a function that returns the largest palindromic number resulting from the product of two-digit numbers."""



def calculate():
    result = []
    for i in range(10,100):
        for j in range(10, 100):
            pal = str(i*j)
            if pal == pal[::-1]:
                result.append(pal)
    return result[-1]


print(calculate())
