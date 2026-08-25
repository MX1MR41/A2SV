# https://codeforces.com/contest/919/problem/D

from collections import defaultdict, deque


n, m = list(map(int, input().split()))

s = input()

g = defaultdict(list)
outdeg = defaultdict(int)

for i in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1

    g[v].append(u)

    outdeg[u] += 1


que = deque()


freqs = defaultdict(lambda: [0] * 26)


for i in range(n):
    if outdeg[i] == 0:
        freqs[i][ord(s[i]) - 97] += 1
        que.append(i)

order = []
res = 0


while que:
    for _ in range(len(que)):
        node = que.popleft()

        order.append(node)

        res = max(res, max(freqs[node]))

        for nei in g[node]:

            for i in range(26):
                freqs[nei][i] = max(freqs[nei][i], freqs[node][i])
            
            outdeg[nei] -= 1

            if outdeg[nei] == 0:
                freqs[nei][ord(s[nei]) - 97] += 1

                que.append(nei)


if len(order) != n:
    print(-1)
else:
    print(res)




