"""

https://codeforces.com/contest/710/problem/B

"""

n = int(input())
arr = list(map(int, input().split()))

arr.sort()


pre = []
p = 0
for i in range(n):
    x = arr[i]
    curr = i*x - p
    pre.append(curr)
    p += x

suff = []
s = 0
for i in range(n - 1, -1, -1):
    x = arr[i]
    curr = -(n - i - 1)*x + s
    suff.append(curr)
    s += x

suff.reverse()


res = [float("inf"), float("inf")]
for i in range(n):
    x = arr[i]
    curr = suff[i] + pre[i]
    if curr < res[1]:
        res = [x, curr]

print(res[0])
