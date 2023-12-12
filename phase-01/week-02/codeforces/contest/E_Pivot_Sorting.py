"""
https://codeforces.com/gym/491508/problem/E

NOT PASSED
"""
from math import ceil
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    maximum = 0
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            maximum = max(maximum, ceil((nums[i] + nums[i + 1]) / 2))    
    for i, num in enumerate(nums):
        nums[i] = abs(num - maximum)
    flag = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            flag = False
            break
    if flag:
        print(maximum)
    else:
        print(-1)