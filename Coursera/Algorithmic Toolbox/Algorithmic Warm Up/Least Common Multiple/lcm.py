# python3
import math


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    return (a * b) / math.gcd(a, b)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(int(lcm(input_a, input_b)))
