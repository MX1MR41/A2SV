"""
https://codeforces.com/gym/491508/problem/D

PASSED
"""

n = int(input())

for _ in range(n):
    ans = 0
    t = int(input())
    arr = list(map(int, input().split()))

    d = {(i , x) : x - i for i,x in enumerate(arr)}
    d2 = {x : 0 for x in d.values()}
    for i in d.values():
        d2[i] += 1



    for i in d2.keys():
        if d2[i] >= 2:
            ans += ((d2[i] * (d2[i] -1)) // (d2[i] - (d2[i] - 1))) // 2


    
    print(ans)