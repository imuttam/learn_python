"""Write a program to find its factor"""

num = int(input('Enter a number to get its factors:  '))

factors = []

for i in range(1, num+1):
    if num%i == 0:
        factors.append(i)

print(f'Factors of {num} are: {factors}')
