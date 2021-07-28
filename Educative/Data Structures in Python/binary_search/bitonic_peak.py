def find_highest_number(A):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low+high)//2

        mid_left = A[mid-1] if mid - 1 > 0 else float('-inf')
        mid_right = A[mid+1] if mid+1 < len(A) else float('inf')

        if A[mid] > mid_left and A[mid] < mid_right:
            low = mid+1
        elif A[mid] < mid_left and A[mid] > mid_right:
            high = mid-1
        elif A[mid] > mid_left and A[mid] > mid_right:
            return A[mid]
    return None

A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))
