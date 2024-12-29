from collections import defaultdict, deque

MOD = 998244353

def mod_inverse(a, mod):
    return pow(a, mod - 2, mod)


t = int(input())
results = []

for _ in range(t):
    n = int(input())
    g = defaultdict(list)
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    
    
    depth = [n + 1] * (n + 1)  
    queue = deque()
    
    
    for i in range(1, n + 1):
        if len(g[i]) == 1:  
            depth[i] = 0
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        for neighbor in g[node]:
            if depth[neighbor] > depth[node] + 1:
                depth[neighbor] = depth[node] + 1
                queue.append(neighbor)
    
    
    probabilities = [0] * (n + 1)
    
    def dfs(node, parent, prob):
        probabilities[node] = prob
        for neighbor in g[node]:
            if neighbor != parent:
                prob_to_parent = (depth[neighbor] * mod_inverse(depth[neighbor] + 1, MOD)) % MOD
                dfs(neighbor, node, (prob * prob_to_parent) % MOD)
    
    dfs(1, -1, 1)  
    
    
    results.append(" ".join(map(str, probabilities[1:])))


print("\n".join(results))

