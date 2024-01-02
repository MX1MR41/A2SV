"""

https://codeforces.com/gym/495129/problem/D

PASSED
"""
t = int(input())
l = []
for _ in range(t):
    l.append(input())

l.sort(key = lambda x: len(x))

for i in range(t-1):
    if l[i] not in l[i+1]:
        print("NO")
        break
else:
    print("YES")
    print(*l, sep = "\n")