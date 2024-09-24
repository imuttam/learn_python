# program to convert temprature in celsius/farenheit

print('If you want to convert into Celsius press "c"\nIf you want to convert into Farenheit press "f" ')

temp = input('Enter "f" or "c": ').lower()

if temp == 'f':
    val = float(input('Enter the temprature value in Celsius: '))
    farenheit = (9/5)*val + 32
    print(f'\tTemprature in farenheit is: {farenheit}°F')

else:
    val = float(input('Enter the temprature value in Farenheit: '))
    celsius = (5/9)*(val-32)
    print(f'\tTemprature in celsius is: {celsius}°C')