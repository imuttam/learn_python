x = 88

def func():
    x = 99

func()
print(x)


def f1():
    x = 92
    def f2():
        print(x)
    f2()
f1()