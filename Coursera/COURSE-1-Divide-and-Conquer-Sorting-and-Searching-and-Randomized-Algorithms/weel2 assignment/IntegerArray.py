with open("IntegerArray.txt") as file:
    arr = [int(x) for x in file]

def countSplitInv(B, C):
    D = []
    i = 0
    j = 0
    inv_count = 0
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1
            inv_count += len(B[i:])
    while i < len(B):
        D.append(B[i])
        i += 1
    while j < len(C):
        D.append(C[j])
        j += 1
    return D, inv_count


def arr_count(arr):
    n = len(arr)
    if n > 1:
        split_position = n // 2
        B, X = arr_count(arr[:split_position])
        C, Y = arr_count(arr[split_position:])
        D, Z = countSplitInv(B, C)
        return D, X+Y+Z
    else:
        return arr, 0
array , result = arr_count(arr)
print(result)