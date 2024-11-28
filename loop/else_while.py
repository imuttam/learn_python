lst = [3,5,7,1,17,41,19]

count = 0
while count<len(lst):
    if lst[count] % 2 == 0:
        print("Its even")
        break
    count += 1

else:
    print("No even in list")