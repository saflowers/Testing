# Populate list with prime numbers
# Since all prime numbers above 2 are odd we can omit evaluating any
# number above that that is even.  We can therefore concentrate on
# determining prime based on: n / (3 .. n // 3) with a step of 2

# Preload list to to simply/minimize calculation effort
n = [0, 1, 2, 3, 5, 7]

for x in range(11, 1000, 2):
    for y in range(3, x // 3, 2):
        if not x % y:
            break
    else:
        n.append(x)
print(n)
