#!/usr/bin/python3

a = [3, 6, 9]
b = [9, 9, 9]


def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        print(arr[i])
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr


print(plus_one(a))
print(plus_one(b))
