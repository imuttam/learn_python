""" program to display stars in right angle traingle """

row = int(input('Enter number of row: '))

for i in range(1, row):
    print(' '*row, end='')
    print('* '*(i))
    row -= 1