def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print(fib(10000))