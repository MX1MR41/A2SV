from collections import defaultdict, deque


n, r = list(map(int, input().split()))
rail = defaultdict(set)
for _ in range(r):
    u, v = list(map(int, input().split()))
    rail[u].add(v)
    rail[v].add(u)

bus = defaultdict(set)
for i in range(1, n+1):
    for j in range(i + 1, n+1):
        if j not in rail[i]:
            bus[i].add(j)
            bus[j].add(i)


busdp = [float("inf")] * (n + 1)
busdp[1] = 0

for _ in range(n):
    currbusdp = busdp[::]
    for i in range(n + 1):
        if currbusdp[i] != float("inf"):
            for nei in bus[i]:
                currbusdp[nei] = min(currbusdp[nei], currbusdp[i] + 1)

    busdp = currbusdp



raildp = [float("inf")] * (n + 1)
raildp[1] = 0

for _ in range(n):
    currraildp = raildp[::]
    for i in range(n + 1):
        if currraildp[i] != float("inf"):
            for nei in rail[i]:
                currraildp[nei] = min(currraildp[nei], currraildp[i] + 1)

    raildp = currraildp


dp1, dp2 = raildp[n], busdp[n]
if dp1 == float("inf") or dp2 == float("inf"):
    print(-1)
else:
    if dp1 == dp2:
        print(dp1 + 1)
    else:
        print(max(dp1, dp2))

