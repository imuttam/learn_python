""" program to display stars in right angle traingle """
row = int(input('Enter number of row: '))
for i in range(1, row):
    for j in range(1, i+1):
        print('*', end='')
    print()