def countways_(bills, amount, maximum, memo):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if (amount, maximum) in memo:
        return memo[(amount, maximum)]

    ways = 0
    for bill in bills:
        if bill <= maximum:
            ways += countways_(bills, amount-bill, bill, memo)

    memo[(amount, maximum)] = ways
    return ways

def countways(bills, amount):
    memo = dict()
    return countways_(bills, amount, max(bills), memo)


print(countways([1,2,5], 5))
