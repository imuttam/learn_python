# Write a program to print ‘F’ to ‘A’ in five different lines.

a = ord('F')
b = ord('A')

for i in range(a,b-1,-1):
    print(chr(i))