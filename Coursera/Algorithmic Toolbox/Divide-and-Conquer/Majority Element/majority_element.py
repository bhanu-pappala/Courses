# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def get_majority(elements):
    length = len(elements)
    if length == 1:
        return elements[0]
    left = get_majority(elements[:length // 2])
    right = get_majority(elements[length // 2:])
    if left == right:
        return left
    else:
        max_left = sum([1 if elements[i] == left else 0 for i in range(length)])
        max_right = sum([1 if elements[i] == right else 0 for i in range(length)])
        if max_left > max_right:
            return left
        else:
            return right


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    result = get_majority(elements)
    count = 0
    length = len(elements)
    for i in range(length):
        if elements[i] == result:
            count += 1
            if count > length / 2:
                return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
