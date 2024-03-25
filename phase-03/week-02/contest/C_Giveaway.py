"""

https://codeforces.com/gym/504939/problem/C

PASSED
"""


n, t = list(map(int, input().split()))
arr = sorted(list(map(int,input().split())))
pre = [0 for _ in range(n)]
p = 0
for i in reversed(range(n)):
    p += arr[i]

    pre[i] = p

pre.reverse()

for _ in range(t):
    res = 0
    x, y = list(map(int, input().split()))
    if x == y:
        res = pre[x-1]
    else:
    
        res = pre[x-1] - pre[x - 1-y]
        
    print(res)