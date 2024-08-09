from collections import deque
for _ in range(int(input())):
    n,m,v = list(map(int,input().split()))
    graph = [[] for i in range(n)]
    degree = [0 for i in range(n)]
    for i in range(n):
        a,b = list(map(int,input().split()))
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
        degree[a - 1] += 1
        degree[b - 1] += 1
    
    que = deque()
    for i in range(len(degree)):
        if degree[i] == 1:
            que.append(i)
    order = []
    while  que:
        cur = que.popleft()
        order.append(cur)
        for child in graph[cur]:
            degree[child] -= 1
            if degree[child] == 1:
                que.append(child)
    
    order = set(order)
    color = [0 for i in range(n)]
    pos = 0
    color[m - 1] = 1
    color[v - 1] = 2
    que.append(m - 1)
    que.append(v - 1)
    while que:
        size = len(que)
        for i in range(size):
            cur = que.popleft()
            for neigh in graph[cur]:
                if color[neigh] == 0:
                    que.append(neigh)
                    color[neigh] = color[cur]
    
    pos  = 0
    for i in range(len(graph)):
        if i not in order and color[i] == 2:
            pos = 1
    if pos and v != m:
        print("YES")
    else:
        print("NO")