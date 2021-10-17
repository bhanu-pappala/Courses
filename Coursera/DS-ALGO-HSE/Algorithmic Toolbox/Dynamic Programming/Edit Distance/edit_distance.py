# python3


def edit_distance(first_string, second_string):
    n = len(first_string) + 1
    m = len(second_string) + 1
    array = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        array[0][i] = i
    for i in range(n):
        array[i][0] = i
    for i in range(1, n):
        for j in range(1, m):
            temp = 0 if first_string[i-1] == second_string[j-1] else 1
            array[i][j] = min([
                array[i][j-1] + 1,
                array[i-1][j] + 1,
                array[i-1][j-1] + temp
            ])
    return array[n-1][m-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
