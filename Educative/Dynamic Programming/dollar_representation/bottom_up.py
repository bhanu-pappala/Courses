def countways(bills, amount):
    if amount <= 0:
        return 0
    
    dp = [[1 for _ in range(len(bills))] for _ in range(amount+1)]

    for amt in range(1, amount+1):
        for j in range(len(bills)):
            bill = bills[j]
            if amt-bill >= 0:
                x = dp[amt-bill][j]
            else:
                x = 0
            
            if j > 0:
                y = dp[amt][j-1]
            else:
                y = 0

            dp[amt][j] = x+y
    return dp

print(countways([1, 2, 5], 5))
