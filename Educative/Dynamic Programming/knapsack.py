def solveKnapsack(weights, prices, capacity, index):
    if capacity <= 0 or index >= len(weights):
        return 0
    if weights[index] > capacity:
        return solveKnapsack(weights, prices, capacity, index + 1)
    return max(prices[index] + solveKnapsack(weights, prices, capacity - weights[index], index + 1), solveKnapsack(weights, prices, capacity, index + 1))

def knapsack(weights, prices, capacity):
    return solveKnapsack(weights, prices, capacity, 0)

print(knapsack([2,1,1,3], [2,8,1,10], 4))