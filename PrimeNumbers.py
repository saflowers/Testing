# Populate list with prime numbers
# Since all prime numbers above 2 are odd we can omit evaluating any
# number above that that is even.  We can therefore concentrate on
# determining prime based on: n / (3 .. (n // 3) + 1) with a step of 2

# Preload list to to simply/minimize calculation effort
n = [0, 2]

for x in range(1, 1000, 2):
    for y in range(3, (x // 3) + 1, 2):
        if not x % y:
            break
    else:
        n.append(x)

n.sort()
print(n)
