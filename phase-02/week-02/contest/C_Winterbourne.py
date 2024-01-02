"""

https://codeforces.com/gym/495129/problem/C

PASSED
"""

t = int(input())

for _ in range(t):
    n , m = list(map(int,input().split())) # n = people, m = chairs
    a = list(map(int, input().split()))
    a.sort()
    if n >= m:
        print("NO")
        continue

    c = m - n # available chairs
    flag = False
    diff = sum(a[1:]) + a[-1]

    if c - diff < 0:
        flag = True
    
    
    if flag:
        print("NO")
    else:
        print("YES")