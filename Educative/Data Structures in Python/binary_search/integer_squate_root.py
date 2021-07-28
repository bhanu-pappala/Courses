def square_root(k):
    low = 0
    high = k

    while low <= high:
        mid = (low+high)//2

        mid_sq = mid * mid

        if mid_sq <= k:
            low = mid+1
        else:
            high = mid-1

    return low - 1

k = 300
print(square_root(k))
