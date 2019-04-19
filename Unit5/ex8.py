numbers = [1, 2, 3, 4]

g = [3 * x for x in numbers]
print(g)

h = [3 * x for x in numbers if x < 2]
print(h)

i = [n + 1 for n in numbers if n >= 1]
print(i)

j = [[x, x ** 2] for x in numbers]
print(j)
