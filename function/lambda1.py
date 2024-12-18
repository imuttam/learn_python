# sorting complex number by distance from origin

def distance(x):
    return x.real**2 + x.imag**2

print(distance(2 + 2j))

l = [1+1j, 2, 0, 2+3j, 4j]

sorted_dist = sorted(l, key=distance)

print(sorted_dist)

