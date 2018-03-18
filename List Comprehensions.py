m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
r = [[x[y] for x in m] for y in range(len(m)+1)]
print(r)
