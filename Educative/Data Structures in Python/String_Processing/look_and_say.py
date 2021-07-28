def next_number(n):
    result = []
    i = 0
    while i < len(n):
        count = 1
        while i + 1 < len(n) and n[i] == n[i+1]:
            i += 1
            count += 1
        result.append(str(count) + n[i])
        i += 1
    return ''.join(result)

s = '1'
print(s)
n = 6
for _ in range(n-1):
    s = next_number(s)
    print(s)

