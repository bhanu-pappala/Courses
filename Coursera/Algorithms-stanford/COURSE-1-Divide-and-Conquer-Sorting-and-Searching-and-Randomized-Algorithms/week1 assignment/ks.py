#!/usr/bin/python3

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    num1 = str(x)
    num2 = str(y)
    max_len = max(len(num1), len(num2))
    split = max_len // 2
    high1, low1 = int(num1[:-split]), int(num1[-split:])
    high2, low2 = int(num2[:-split]), int(num2[-split:])
    a = karatsuba(low1, low2)
    b = karatsuba((low1+high1), (low2+high2))
    c = karatsuba(high1, high2)

    result = (c * 10 ** (2 * split)) + ((b-a-c) * 10 ** (split)) + a

    return result

x = int(3141592653589793238462643383279502884197169399375105820974944592)
y = int(2718281828459045235360287471352662497757247093699959574966967627)

print(karatsuba(x, y))