# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    n = len(weights)
    capacity += 1
    array = [[0 for _ in range(capacity)] for _ in range(n)]
    for i in range(capacity):
        if weights[0] < i:
            array[0][i] = weights[0]
    for i in range(1, n):
        for j in range(1, capacity):
            if weights[i] <= j:
                array[i][j] = max(array[i - 1][j], array[i - 1][j - weights[i]] + weights[i])
            else:
                array[i][j] = array[i - 1][j]
    return array[n - 1][capacity - 1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
