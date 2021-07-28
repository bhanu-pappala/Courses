#!/usr/bin/python3
array = [6, 3, 2, 7, 5, 5, 8]

array = sorted(array)

for i in range(len(array)//2):
    print(array[i], array[~i])
