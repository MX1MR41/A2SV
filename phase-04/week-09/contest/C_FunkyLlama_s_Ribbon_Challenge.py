"""

https://codeforces.com/gym/523525/problem/C

PASSED
"""
n, a, b, c = list(map(int, input().split()))
arr = list(set([a, b, c]))
dp = [-1] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in arr:
        left = i - j
        if left >= 0 and dp[left]!= -1:
            if dp[i] == -1:
                dp[i] = 1 + dp[left]
            else:
                dp[i] = max(dp[i], 1 + dp[left])
print(dp)
print(dp[n])