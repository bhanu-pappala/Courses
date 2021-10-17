# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    per_weight = [int(a) / int(b) for a, b in zip(prices, weights)]
    value = 0

    while capacity > 0 and max(per_weight) != -1:
        index = per_weight.index(max(per_weight))
        if weights[index] > capacity:
            value += per_weight[index] * capacity
        else:
            value += prices[index]
        capacity -= weights[index]
        per_weight[index] = -1

    return value

# print(maximum_loot_value(10, [30], [500]))
if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
