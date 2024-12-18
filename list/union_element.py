"""program to find union of two list"""


lst1 = [11,23,45,34,67,68]
lst2 = [32,11,27,45,87,68]


common_list = lst1[:]

for numbers in lst2:
    if numbers not in common_list:
        common_list.append(numbers)

print(lst1)
print(common_list)
