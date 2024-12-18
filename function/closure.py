x = 100

def func1():
    def func2():
        print(x)
    return func2

action = func1()
print(action)
action()
