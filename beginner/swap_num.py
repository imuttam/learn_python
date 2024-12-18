# program to swap value of two number stored in variable

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(f'Before Swapping: \n\tValue of num1 is:{num1}\n\tValue of num2 is: {num2}')

temp = num1
num1 = num2
num2 = temp

print(f'After Swapping: \n\tValue of num1 is:{num1}\n\tValue of num2 is: {num2}')