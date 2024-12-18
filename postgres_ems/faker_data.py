from faker import Faker
f = Faker()

data = dir(f)

for d in data:
    print(d)
    try:
        print(f.d())
    except AttributeError:
        pass
        