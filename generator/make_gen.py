"""making own range generator"""

def my_range(start=0,step=1, stop=10):
    num = start
    while num < stop:
        yield num
        num += step


gen_10 = my_range(10,3,74)
for num in gen_10:
    print(num, end=' ')