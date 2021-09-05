#!/usr/bin/python3

def count_ways_(bills, amount, maximum):
    if amount == 0:
        return 1
    ways = 0
    for bill in bills:
        if bill <= maximum and amount - bill >= 0:
            ways += count_ways_(bills, amount-bill, bill)
    return ways

def count_ways(bills, amount):
    return count_ways_(bills, amount, max(bills))


print(count_ways([1,2,5], 5))
