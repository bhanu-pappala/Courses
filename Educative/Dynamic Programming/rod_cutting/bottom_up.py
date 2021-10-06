def rodCutting(n, prices):
    if n < 0:
        return 0

    dp = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        max_value = 0
        for j in range(i):
            max_value = max(max_value, prices[j] + dp[i-j-1])
        dp[i] = max_value

    return dp[n]


print(rodCutting(3, [3,7,8]))
