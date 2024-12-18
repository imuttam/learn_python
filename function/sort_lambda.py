# sorting using first character using lambda

fruits = ['banana', 'Apple', 'melon', 'Chiku', 'Mango','jackfruit','orange']

print(sorted(fruits))

my_sort1 = sorted(fruits, key=lambda x:x.upper())
my_sort2 = sorted(fruits, key=lambda x:x[-1])# maintain order if collide
my_sort3 = sorted(fruits, key=lambda x:x[1].upper())


print(my_sort1)
print(my_sort2)
print(my_sort3)