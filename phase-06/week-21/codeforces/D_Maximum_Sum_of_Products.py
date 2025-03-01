"""

https://codeforces.com/contest/1519/problem/D

"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

prods = [i*j for i, j in zip(a, b)]
res = sum(prods)


pre = []
suf = []
p = 0
for i in range(n):
    pre.append(p)
    p += a[i]*b[i]

s = 0
for j in range(n -1, -1, -1):
    suf.append(s)
    s += a[j]*b[j]

suf.reverse()

for i in range(n):
    l,  r = i, i + 1
    curr = 0
    while l >= 0 and r < n:
        curr += a[l]*b[r] + a[r]*b[l]
        res = max(res, pre[l] + curr + suf[r])
        l -= 1
        r += 1


for i in range(n):
    l,  r = i- 1, i
    curr = a[i]*b[i]
    l, r = i - 1, i + 1
    while l >= 0 and r < n:
        curr += a[l]*b[r] + a[r]*b[l]
        res = max(res, pre[l] + curr + suf[r])
        l -= 1
        r += 1
print(res)
