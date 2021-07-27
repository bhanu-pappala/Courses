def lcs(str1: str, str2: str) -> int:
    n = len(str1)
    m = len(str2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    max_length = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(dp[i][j], max_length)
            else:
                dp[i][j] = 0
    return max_length


# print(lcs("hel", "elf"))

import random
import string

st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(400))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(600))
print(lcs(st1, st2))
