def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            return False

    return True

def is_perm_2(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    ht = dict()

    for i in str_1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in str_2:
        if i in ht:
            ht[i] -= 1
        else:
            return False
    return all(value == 0 for value in ht.values())

is_permutation_1 = "google"
is_permutation_2 = "ooggle"

not_permutation_1 = "not"
not_permutation_2 = "top"
print(is_perm_1(is_permutation_1, is_permutation_2))
print(is_perm_1(not_permutation_1, not_permutation_2))

print(is_perm_2(is_permutation_1, is_permutation_2))
print(is_perm_2(not_permutation_1, not_permutation_2))
    
