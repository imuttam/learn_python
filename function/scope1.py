x = 90

def fun1():
    x = 80
    def fun2():
        print(x)

    fun2()

fun1()

y = 92
def fun3(w):
    z = w+y
    return z

print(fun3(8))