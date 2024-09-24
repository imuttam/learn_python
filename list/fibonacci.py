"""program to generate fibonacci series"""

num = int(input('Enter a range to generate fibonacci: '))
a = 0
b = 1

count = 0

while count < num:
    print(b, end= ' ')
    a, b = b, a+b
    count += 1
