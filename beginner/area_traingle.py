# Program to find Area of traingle

a = float(input('Enter first side of the traingle: '))
b = float(input('Enter second side of the traingle: '))
c = float(input('Enter third side of the traingle: '))

S = (a+b+c)/2

Area = (S*(S-a)*(S-b)*(S-c))**0.5

print(f'Area of given traingle is: {Area:.2f}')