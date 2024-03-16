"""

https://codeforces.com/gym/503628/problem/E

PASSED
"""

t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    pos = 1
    if nums[0] != 1:
        pos = 0
    total = 1
    for i in range(1,n):
        if nums[i] > total:
            pos = 0
            break
        total += nums[i]
    if pos:
        print("YES")
    else:
        print("NO")