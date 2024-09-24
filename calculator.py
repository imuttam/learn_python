"""write a program to make a calculator"""

while True:
    print("pl. enter two numbers seperated by space: ")
    nums = input()
    try:
        nums = nums.split()
        a = int(nums[0])
        b = int(nums[1])

        print("######################################################################")
        choice = input('\tEnter 1 to add above two numbers\n\tEnter 2 to get diference between numbers\n\tEnter 3 to multiply above two numbers\n\tEnter anything else to quit.\n"######################################################################"\n')

        if choice == '1':
            print( a+b )

        elif choice == '2':
            print(abs(a-b))

        elif choice == '3':
            print(a*b)
    except:
        print('you have given wrong input, thanks for playing.')
        break

