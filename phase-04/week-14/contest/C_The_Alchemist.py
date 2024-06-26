import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().split()
index = 0

test_cases = int(data[index])
index += 1

results = []

for _ in range(test_cases):
    n = int(data[index])
    k = int(data[index + 1])
    index += 2

    cost = [0] + list(map(int, data[index : index + n]))
    index += n

    nums = set(map(int, data[index : index + k]))
    index += k

    graph = defaultdict(list)
    degree = [0] * (n + 1)
    future = [0] * (n + 1)
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        m = int(data[index])
        edges = list(map(int, data[index + 1 : index + 1 + m]))
        index += 1 + m
        if i in nums:
            continue
        degree[i] = m
        for a in edges:
            graph[a].append(i)

    queue = deque()
    for node in range(1, n + 1):
        if node in nums:
            queue.append(node)
        elif degree[node] == 0:
            ans[node] = cost[node]
            queue.append(node)

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            degree[child] -= 1
            future[child] += ans[node]
            if degree[child] == 0:
                queue.append(child)
                ans[child] = min(cost[child], future[child])

    results.append(" ".join(map(str, ans[1:])))

print("\n".join(results))
