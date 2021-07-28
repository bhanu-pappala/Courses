def is_palin_perm(input_str):
    input_str = input_str.replace(' ', '').lower()

    d = dict()
    for i in input_str:
        if i in d:
            d[i] += 1
        else :
            d[i] = 1

    odd_count = 0
    for key, value in d.items():
        if value%2 != 0 and odd_count == 0:
            odd_count += 1
        elif value%2 != 0 and odd_count != 0:
            return False
    return True

palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))
