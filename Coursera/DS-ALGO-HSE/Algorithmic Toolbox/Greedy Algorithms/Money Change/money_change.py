# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    if money == 0:
        return 0
    count = 0
    value = 0
    for i in [10, 5, 1]:
        if money >= i:
            rem = money // i
            count += rem
            money = money % i
            if money == 0:
                return count
                break


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
