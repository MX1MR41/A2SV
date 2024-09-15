from collections import defaultdict, deque


for _ in range(int(input())):

   n = int(input())
   a = list(map(int, input().split()))
   d = defaultdict(list)
  
   for i in range(n - 1):
       d[i + 2].append(a[i])
       d[a[i]].append(i + 2)
  
   queue = deque([(1, 1)])
   level = [0] * (n + 1)
   v = [0] * (n + 1)
  
   while queue:
       x, y = queue.popleft()
       level[y] += 1
       v[x] = 1
       for i in d[x]:
           if v[i] == 0:
               queue.append((i, y + 1))
  
   ans = 0
   unpaired = 0
  
   for i in range(n, 1, -1):
       if level[i] > 1:
           x = min(unpaired, level[i] - 1)
           ans += x
           unpaired -= x
           level[i] -= x
       ans += level[i] // 2
       unpaired += level[i] % 2
  
   print(ans)