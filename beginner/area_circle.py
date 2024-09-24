# Program to find Area and Perimeter of circle

from math import pi

radius = float(input('Enter radius of circle: '))

circumference = 2*pi*radius
area = pi*radius*radius

print(f'Area of given circle is: {area:.2f} unit and circumference is {circumference:.2f} unit.')