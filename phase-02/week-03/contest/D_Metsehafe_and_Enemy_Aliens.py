"""

https://codeforces.com/gym/496610/problem/D
"""
from math import ceil
t = int(input())
for _ in range(t):
    n = int(input())
    nums = sorted(map(int, input().split()))
    ans = 0
    cur = 0
    left = 0
    right = n - 1
    while left < right:
        cur += nums[left]
        if cur >= nums[right]:
            ans += nums[right] + 1
            cur -= nums[right]
            right -= 1
        left += 1
    if left == right:
        cur += nums[right]
    ans += (ceil(cur / 2) + 1) if cur > 1 else cur
    print(ans)