# https://atcoder.jp/contests/dp/tasks/dp_f

s = input().strip()
t = input().strip()
len_s, len_t = len(s), len(t)

dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]
# find length of longest subsequence
for i in range(1, len_s + 1):
    for j in range(1, len_t + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

i, j = len_s, len_t
lcs = []
# reconstruct string from the dp table
while i > 0 and j > 0:
    if s[i - 1] == t[j - 1]:
        lcs.append(s[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(''.join(reversed(lcs)))
