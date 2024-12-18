
def average(*args):
    print(args)
    return sum(args)/len(args)


print(average(1,2,3,4,5))