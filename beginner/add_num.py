# a programme to add numbers given input by user

numberOfNumbers = int(input('Enter how many number you want to add: '))
total = 0

for i in range(numberOfNumbers):
    num = int(input(" Enter number: "))
    total += num

print(f'Sum of all numbers are: {total}')