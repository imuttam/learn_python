# write a program to check weather its a leap year or not

year = int(input('Enter year: '))

if (year % 100 == 0) and (year % 400 == 0):
    print(f'{year} is a leap year.')

elif (year % 100 != 0) and (year % 4 == 0):
    print(f'{year} is a leap year.')

else:
    print(f'{year} is a not a leap year.')