"""

https://codeforces.com/gym/504939/problem/D

PASSED
"""

from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    cnt1 = defaultdict(int)
    l = 0
    for r in range(n):
        if arr1[r] != arr1[l]:
            l = r 

        cnt1[arr1[r]] = max(cnt1[arr1[r]], r - l +1)


    cnt2 = defaultdict(int)
    l = 0
    for r in range(n):
        if arr2[r] != arr2[l]:
            l = r

        cnt2[arr2[r]] = max(cnt2[arr2[r]], r - l +1)

    res = 0
    for i in cnt1:
        res = max(res, cnt1[i]+cnt2[i])
    for i in cnt2:
        res = max(res, cnt1[i]+cnt2[i])

    print(res)
        




    