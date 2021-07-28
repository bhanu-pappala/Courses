#!/usr/bin/env python

array = [-2, 1, 2, 4, 7, 11]
target = 13


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(arr, target):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j])
                return True
    return False


# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_table(arr, target):
    ht = dict()
    for i in range(len(arr)):
        if arr[i] in ht:
            print(ht[arr[i]], arr[i])
            return True
        else:
            ht[target - arr[i]] = arr[i]
    return False


# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(arr, target):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])
            return True
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
    return False


print(two_sum_brute_force(array, target))
print(two_sum_hash_table(array, target))
print(two_sum(array, target))
