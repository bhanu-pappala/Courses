# python3


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m ** 2):
        previous, current \
            = current, (previous + current) % m

        if previous == 0 and current == 1:
            return i + 1


def helper_fib(n):
    if n <= 1:
        return n

    return helper_fib(n - 1) + helper_fib(n - 2)


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    temp = helper_fib(n)
    return temp % m


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    pis = pisano_period(m)
    n = n % pis

    last_second = 0
    last = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(1, n):
        last_second, last = last, last + last_second

    return last % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
