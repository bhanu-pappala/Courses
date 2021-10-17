# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def compare(digit1, digit2):
    if int(str(digit1) + str(digit2)) > int(str(digit2) + str(digit1)):
        return digit1
    else:
        return digit2


def largest_number(numbers):
    result = ""
    while len(numbers) > 0:
        temp = 0
        for digit in numbers:
            temp = compare(temp, digit)
        numbers.remove(temp)
        result += str(temp)
    return result


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
