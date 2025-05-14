def pythagorean_triple(integers):
    integers.sort()
    a,b,c = integers
    return a**2 + b**2 == c**2