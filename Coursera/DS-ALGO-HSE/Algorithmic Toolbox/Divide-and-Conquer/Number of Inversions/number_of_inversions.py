# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    if len(a) == 1:
        return 0
    mid = len(a)//2
    left, right = a[:mid], a[mid:]
    count = compute_inversions(left) + compute_inversions(right)
    left.sort()
    right.sort()
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            count += len(left) - i
            j += 1
        else:
            i += 1
    return count


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
