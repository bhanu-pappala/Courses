def permutations(str):
    if str == "":
        return [""]
    permuts = []
    for char in str:
        sub_permuts = permutations(str.replace(char, "", 1))
        for each in sub_permuts:
            permuts.append(char + each)
    return permuts

str = "abc"
print(permutations(str))