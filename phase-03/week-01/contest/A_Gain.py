"""

https://codeforces.com/gym/503628/problem/A

PASSED
"""

t = int(input())

for  _ in range(t):
    res = []
    n = int(input())
    arr = list(map(int, input().split()))
    M = max(arr)

    sortedarr = sorted(arr)
    
    M2 = sortedarr[-2]

    for i in arr:
        if i == M:
            res.append(i - M2)
        else:
            res.append(i - M)

    print(*res, sep = ' ')

