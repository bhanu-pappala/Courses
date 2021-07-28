import bisect

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

print(A)

print("This is bisect left")
print(bisect.bisect_left(A, -10))
print(bisect.bisect_left(A, 285))

print("\n")
print("This is bisect right")
print(bisect.bisect_right(A, -10))
print(bisect.bisect_right(A, 285))

print("\n")
print("This is bisect")
print(bisect.bisect(A, -10))
print(bisect.bisect(A, 285))

print('\n')
print(A)

print("\n")
print("This is insort right")
bisect.insort_right(A, 108)
print(A)

print("\n")
print("This is insort left")
bisect.insort_left(A, 108)
print(A)
