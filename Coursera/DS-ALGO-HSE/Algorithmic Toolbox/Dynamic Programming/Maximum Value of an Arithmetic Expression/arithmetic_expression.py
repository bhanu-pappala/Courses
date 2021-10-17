# python3
import math


def do_op(a,b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def maxandmin(mins, maxs, ops, i, j):
    r_min = math.inf
    r_max = -1 * math.inf
    for k in range(i,j):
        a = do_op(maxs[i][k], maxs[k+1][j], ops[k])
        b = do_op(maxs[i][k], mins[k+1][j], ops[k])
        c = do_op(mins[i][k], mins[k+1][j], ops[k])
        d = do_op(mins[i][k], maxs[k+1][j], ops[k])
        r_min = min(r_min, a, b, c, d)
        r_max = max(r_max, a, b, c, d)
    return r_min, r_max

def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    nums = []
    ops = []
    for i in range(len(dataset)):
        if '0' <= dataset[i] <= '9':
            nums.append(int(dataset[i]))
        else:
            ops.append(dataset[i])
    n = len(nums)
    mins = [[0 for _ in range(n)] for _ in range(n)]
    maxs = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mins[i][i] = nums[i]
        maxs[i][i] = nums[i]
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            mins[i][j], maxs[i][j] = maxandmin(mins, maxs, ops, i, j)
    return maxs[0][n - 1]


if __name__ == "__main__":
    print(find_maximum_value(input()))
