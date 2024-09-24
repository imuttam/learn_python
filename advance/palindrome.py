"""Implement a function that returns the number of all three-digit palindromic numbers."""

lst = []
for num in range(100,1000):

    if str(num) == str(num)[::-1]:
        lst.append(num)

print(len(lst))