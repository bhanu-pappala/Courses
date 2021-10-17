# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    f = len(first_sequence) + 1
    s = len(second_sequence) + 1
    t = len(third_sequence) + 1
    array = [[[0 for _ in range(t)] for _ in range(s)] for _ in range(f)]
    for i in range(1, f):
        for j in range(1, s):
            for k in range(1, t):
                temp = 1 if first_sequence[i-1] == second_sequence[j-1] == third_sequence[k-1] else 0
                array[i][j][k] = max(array[i][j][k-1],
                                     array[i][j-1][k],
                                     array[i-1][j][k],
                                     array[i-1][j-1][k-1] + temp)
    return array[f-1][s-1][t-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
