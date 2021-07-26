# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def generate_periodic_path():
    f_mod_10 = [0] * 60
    f_mod_10[0], f_mod_10[1] = 0, 1
    for i in range(2, 60):
        f_mod_10[i] = (f_mod_10[i-1] + f_mod_10[i-2]) % 10
    return f_mod_10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    f_mod_10 = generate_periodic_path()
    answer = (f_mod_10[n % 60] * f_mod_10[(n+1) % 60]) % 10
    return answer



if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
