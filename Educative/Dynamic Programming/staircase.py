def staircase(n, m):
    if n <= 0:
        return 1
    ways = 0
    for i in range(1, m+1):
        if  i <= n:
            ways += staircase(n-i, m)
    return ways

print(staircase(4,2))