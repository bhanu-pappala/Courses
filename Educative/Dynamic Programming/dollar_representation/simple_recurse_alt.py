#!/usr/bin/python3

def count_ways_(bills, amount , index):
    if amount == 0:
        return 1
    if amount < 0 or index >= len(bills):
        return 0
    return count_ways_(bills, amount-bills[index], index) + count_ways_(bills, amount, index+1)

def count_ways(bills, amount):
    return count_ways_(bills, amount, 0)

print(count_ways([1,2,5], 5))

