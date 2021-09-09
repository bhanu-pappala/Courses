import copy

def merge(arr, sortedArray, low, mid, high):
    k = i = low
    j = mid + 1
    inv_count = 0
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            sortedArray[k] = arr[i]
            i += 1
        else:
            sortedArray[k] = arr[j]
            inv_count += (mid + 1 - i)
            j += 1

        k += 1

    while i <= mid:
        sortedArray[k] = arr[i]
        k += 1
        i += 1

    for i in range(low, high + 1):
        arr[i] = sortedArray[i]

    return inv_count



def mergesort(arr, sortedArray, low, high):
    if high == low:
        return 0
        print(high, low)
    mid = (low + high) // 2
    inv_count = 0


    inv_count += mergesort(arr, sortedArray, low, mid)
    inv_count += mergesort(arr, sortedArray, mid+1, high)
    print(*sortedArray)
    inv_count += merge(arr, sortedArray, low, mid, high)

    return inv_count


array = [5, 3, 8, 9, 1, 7, 0, 2, 6, 4]
sortedArray = list(array).copy()
n = len(array)
result = mergesort(array, sortedArray, 0, n-1)
print(result)