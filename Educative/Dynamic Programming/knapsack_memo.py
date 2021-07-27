def solveknapsack(weights, prices, capacity, index, memo):
    if capacity <= 0 or index >= len(weights):
        return 0
    if (capacity, index) in memo:
        return memo[(capacity, index)]
    if weights[index] > capacity:
        memo[(capacity, index)] = solveknapsack(weights, prices, capacity, index + 1, memo)
        return memo[capacity, index]
    memo[(capacity, index)] =  max(prices[index] + solveknapsack(weights, prices, capacity - weights[index], index + 1, memo), solveknapsack(weights, prices, capacity, index + 1, memo))
    return memo[(capacity, index)]

def knapsack(weights, prices, capacity):
    memo = {}
    return solveknapsack(weights, prices, capacity, 0, memo)

print(knapsack([2,1,1,3], [2,8,1,10], 4))