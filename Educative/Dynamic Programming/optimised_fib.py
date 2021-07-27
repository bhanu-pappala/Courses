def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    secondLast = 0
    last = 1
    current = None
    for i in range(1, n):
        current = secondLast + last
        secondLast = last
        last = current
    return current



print(fib(10000))