"""

https://codeforces.com/gym/523525/problem/D

PASSED
"""

from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
nums = sorted(list(set(arr)))
# print(nums)
cnt = Counter(arr)

dp = [0] * (max(arr) + 1)
dp[1] = cnt[1]

for i in range(2, max(arr) + 1):
    dp[i] = max(dp[i-1], dp[i-2] + i * cnt[i])

print(dp[-1])