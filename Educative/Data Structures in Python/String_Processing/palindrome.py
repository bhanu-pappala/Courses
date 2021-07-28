def solution1(s):
    s = ''.join([i for i in s if i.isalnum()]).replace(' ', '').lower()
    return s == s[::-1]

def solution2(s): #preferred
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

s = "Was it a cat I saw?"
print(solution1(s))
print(solution2(s))
