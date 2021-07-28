def array_advance(arr):
    furthest_reached = 0
    last_ind = len(arr) - 1
    i = 0
    while i <= furthest_reached < last_ind:
        furthest_reached = max(furthest_reached, arr[i] + i)
        i += 1
    return furthest_reached >= last_ind

A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))
