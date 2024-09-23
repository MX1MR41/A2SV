from collections import defaultdict, deque


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    has = list(map(int, input().split()))
    mix = defaultdict(list)



    for potion in range(n):
        need = list(map(int, input().split()))
        if need[0]: mix[potion] = [i - 1 for i in need[1:]]

    g = defaultdict(list)
    deg = defaultdict(int)
    for p, ingredients in mix.items():
        for ing in ingredients:
            g[ing].append(p)
            deg[p] += 1
    # print("graph", g)
    # print("deg", deg)
    
    dp = coins[::]
    for i in has: dp[i-1] = 0

    def cost(potion):
        if potion in mix: return min(dp[potion], sum(dp[i] for i in mix[potion]))
        else: return dp[potion]

    # print("-"*50)

    que = deque()
    for i in range(n):
        if not deg[i]: que.append(i)

    while que:
        for _ in range(len(que)):
            curr = que.popleft()
            dp[curr] = cost(curr)
            for nei in g[curr]:
                deg[nei] -= 1
                if not deg[nei]:
                    que.append(nei)

    print(*dp)



