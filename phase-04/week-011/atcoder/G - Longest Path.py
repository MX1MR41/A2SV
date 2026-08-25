# topological sort + dp
# sort topologically to find the base-case i.e. leaf nodes
# then calculate their dp then build up

from collections import defaultdict, deque

g = defaultdict(list) # store graph with nodes reversed to help with top-sort traversal
g2 = defaultdict(list) # stores actual graph
dp = defaultdict(int)
deg = defaultdict(int) # out-degree
N, M = list(map(int, input().split()))

for i in range(M):
  u, v = list(map(int, input().split()))
  g[v].append(u)
  g2[u].append(v)
  deg[u] += 1
 
def find(x):
  curr = 0
  neis = g2[x]
  for nei in neis:
    curr = max(curr, 1 + dp[nei])
    
  dp[x] = curr
  
  
que = deque()
for i in range(1, N+1):
  if deg[i] == 0:
    que.append(i)
 

while que:
  for _ in range(len(que)):
    node = que.popleft()
    find(node)
    neis = g[node]
    for nei in neis:
      deg[nei] -= 1
      if deg[nei] == 0:
        que.append(nei)
        
print(max(dp.values()))

  

    
  
  
