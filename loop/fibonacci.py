# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# count = 0
# while count < n:
    # print(a)
    # a, b = b, a + b
    # count += 1
a,b = 0,1
for i in range(10):
    print(a, end=" ")
    a,b = b, a+b 

