# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    n = len(first_sequence) + 1
    m = len(second_sequence) + 1
    array = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            temp = 1 if first_sequence[i - 1] == second_sequence[j - 1] else 0
            array[i][j] = max(array[i - 1][j], array[i][j - 1], array[i - 1][j - 1] + temp)

    return array[n - 1][m - 1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
