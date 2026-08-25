"""

https://codeforces.com/contest/1203/problem/F1

"""
n, r = list(map(int, input().split()))
pos = []
neg = []
for _ in range(n):
    j, d = list(map(int, input().split()))
    if d >= 0:
        pos.append((j, d))
    else:
        neg.append((j, d))

pos.sort()

can = True

for j, d in pos:
    if r < j or r < 0:
        can = False
        break
    r += d

if not can:
    print("NO")
    exit()

neg.sort(key = lambda x: sum(x), reverse=True)

for j, d in neg:
    if r < j or r < 0:
        can = False
        break
    r += d

if not can or r < 0:
    print("NO")
else:
    print("YES")
