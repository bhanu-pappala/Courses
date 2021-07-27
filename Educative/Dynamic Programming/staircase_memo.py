def nthstair(n, m, memo):
    if n <= 0:
        return 1
    if n in memo:
        return memo[n]
    ways = 0
    for i in range(1, m+1):
        if i <= n:
            ways += nthstair(n-i, m, memo)
    memo[n] = ways
    return ways

def staircase(n, m):
    memo = {}
    return nthstair(n, m, memo)


print(staircase(99,2))