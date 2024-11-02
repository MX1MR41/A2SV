import heapq


t = int(input())
for _ in range(t):
    
    n, m = map(int, input().split())
    
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    
    s = list(map(int, input().split()))
    
    
    dist = [[float("inf")] * 1001 for _ in range(n)]
    vis = [[False] * 1001 for _ in range(n)]
    
    
    dist[0][s[0]] = 0
    q = []
    heapq.heappush(q, (0, 0, s[0]))  
    
    
    while q:
        d, u, k = heapq.heappop(q)
        d = -d  
        
        
        if vis[u][k] or dist[u][k] == float("inf"):
            continue
        
        vis[u][k] = True
        
        
        for v, w in adj[u]:
            
            new_speed = min(s[v], k)
            new_dist = d + w * k
            
            
            if dist[v][new_speed] > new_dist:
                dist[v][new_speed] = new_dist
                heapq.heappush(q, (-new_dist, v, new_speed))
    
    
    ans = min(dist[n - 1][k] for k in range(1, 1001))
    print(ans)
