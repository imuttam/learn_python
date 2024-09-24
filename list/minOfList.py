"""Finding minimum number in a list"""

#create a list
lst = []
while True:
    num = input()
    if num == 'q':
        break
    else:
        lst.append(int(num))


print(f'Your list is: {lst}')

mini = lst[0]

for i in range(len(lst)):
    if lst[i] <  mini:
        mini = lst[i]

print(f'Minimum number in the list {lst} is {mini}')