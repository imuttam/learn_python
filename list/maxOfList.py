"""Finding maximum number in a list"""

#create a list
lst = []
while True:
    num = input()
    if num == 'q':
        break
    else:
        lst.append(int(num))


print(f'Your list is: {lst}')

maxi = lst[0]

for i in range(len(lst)):
    if lst[i] > maxi:
        maxi = lst[i]

print(f'Maximum number in the list {lst} is {maxi}')