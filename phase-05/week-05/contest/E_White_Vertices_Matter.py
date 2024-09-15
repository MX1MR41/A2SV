from collections import defaultdict, deque
   
n = int(input().strip())
dp = list(map(int, input().strip().split()))

for i in range(n):
    if dp[i] == 0:
        dp[i] = -1

g = defaultdict(list)
for _ in range(n - 1):
    u, v  = map(int, input().strip().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

queue = deque()
queue.append((0, -1))
i = 0

while i < len(queue):
    le =  len(queue)
    for _ in range(i, le):
        cur, par = queue[i]
        i += 1
        for ne in g[cur]:
            if ne != par:
                queue.append((ne, cur))

for i in range(len(queue) -1,0, -1):
    dp[queue[i][1]] += max(0, dp[queue[i][0]])

queue = [(0, -1)]
while queue:
    le = len(queue)
    for _ in range(le):
        cur, par = queue.pop()
        for ne in g[cur]:
            if ne != par:
                dp[ne] += max(0, dp[cur]  - max(0, dp[ne]))
                queue.append((ne, cur))
print(*dp)