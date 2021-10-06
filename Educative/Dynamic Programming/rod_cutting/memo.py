def rodCutting_(n, prices, memo):
    if n < 0:
        return 0

    if n in memo:
        return memo[n]

    max_value = 0
    for i in range(1, n+1):
        max_value = max(max_value, prices[i-1] + rodCutting_(n-i, prices, memo))

    memo[n] = max_value
    return memo[n]


def rodCutting(n, prices):
    memo = {}
    return rodCutting_(n, prices, memo)


print(rodCutting(3, [3,7,8]))
