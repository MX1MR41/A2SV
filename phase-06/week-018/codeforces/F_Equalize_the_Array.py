"""
https://codeforces.com/contest/1490/problem/F
"""

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    
    cnt = Counter(a)

    
    freqs = Counter(cnt.values())

    
    arr = sorted(freqs.items())  

    res = n
    left = 0
    right = n  
    rightCnt = len(cnt)  

    for f, c in arr:
        
        res = min(res, left + right - (rightCnt * f))

        
        left += f * c
        right -= f * c
        rightCnt -= c

    print(res)


