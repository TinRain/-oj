
a = [1, 2, 3, 4, 5, 6, 9, 32, 12, 35, 56, 20]
n = 22

a.sort()

b = [n-x for x in a]
print(b)
b.reverse()

res = False

index = 0

