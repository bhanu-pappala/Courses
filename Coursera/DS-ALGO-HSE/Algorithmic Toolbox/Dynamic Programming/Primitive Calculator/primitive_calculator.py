# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    array = [0] + [n] * n
    operations = ['1', '2', '3']
    for i in range(n):
        for operation in operations:




if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)





