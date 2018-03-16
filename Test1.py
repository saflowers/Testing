def f(x):
    return not (x % 3) or not (x % 5)


s = filter(f, range(2, 21))
for x in s:
    print(x, sep='.', end=' ')

