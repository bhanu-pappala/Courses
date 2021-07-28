def recursive_multiply(x, y):
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)

x = 500
y = 2000


print(x*y)
print(recursive_multiply(x, y))
