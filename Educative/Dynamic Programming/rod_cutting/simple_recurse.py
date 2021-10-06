def rodCutting(n, prices):
    if n < 0:
        return 0

    max_value = 0
    for i in range(1, n+1):
        max_value = max(max_value, prices[i-1] + rodCutting(n-i, prices))
    return max_value

print(rodCutting(3, [3,7,8]))
