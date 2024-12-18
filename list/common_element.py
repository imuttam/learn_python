
lst1 = [11,23,45,34,67,68]
lst2 = [32,11,27,45,87,68]

common = []

for elem in lst1:
    if elem in lst2:
        common.append(elem)

print(common)