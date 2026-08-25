n, m = map(int, input().split())
a = list(map(int, input().split()))
l = [0] + [max(0, a[i] - a[i + 1]) for i in range(n - 1)]
r = [0] + [max(0, a[i] - a[i - 1]) for i in range(1, n)]
for i in range(n - 1):
    l[i + 1] += l[i]
    r[i + 1] += r[i]
for _ in range(m):
    s, t = map(int, input().split())
    if s < t:
        print(l[t - 1] - l[s - 1])
    else:
        print(r[s - 1] - r[t - 1])