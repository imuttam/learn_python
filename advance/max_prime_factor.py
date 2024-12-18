""" implement a function that takes a natural number as an argument and returns the greatest prime factor of that number. """

num = int(input("Enter a number to get its prime factor: "))

def isPrime(n):
    r = int(n**0.5+1)
    for i in range(2, r):
        if n % i == 0:
            return False
            break
    return True

def factor(num):

    lst = []
    for i in range(2, num//2):
        if num%i == 0:
            lst.append(i)
    # lst = lst[::-1]
    # for numbers in lst:
    #     if isPrime(numbers):
    #         return numbers
    return lst


print(factor(num))

number = int(input("Enter a number to get its prime factor: "))

def calculate(number):
    i = 2
    factors = []
    while i * i <= number:
        if not number % i == 0:
            i += 1
        else:
            number = number // i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return (factors)

print(calculate(number))