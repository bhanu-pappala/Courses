#!/usr/bin/python3
A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
B = [20, 66, 12, 48, 38, 38, 20, 65, 54]
def buy_and_sell_once(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(profit, max_profit)
    return max_profit

print(buy_and_sell_once(B))
