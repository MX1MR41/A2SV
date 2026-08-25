# https://atcoder.jp/contests/dp/tasks/dp_p

import sys
from collections import defaultdict

MOD = 10**9 + 7

# Input reading
n = int(input())
graph = defaultdict(list)

# Reading tree edges
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Stack for iterative DFS
stack = [(1, -1)]  # (current node, parent)
# We need a separate stack to emulate post-order traversal to calculate DP in bottom-up fashion.
postorder_stack = []

# Initialize dp table with placeholders for white and black counts
dp = [[1, 1] for _ in range(n+1)]  # dp[i][0]: white, dp[i][1]: black

# Iterative DFS to generate post-order traversal
while stack:
    node, parent = stack.pop()
    postorder_stack.append((node, parent))
    
    for neighbor in graph[node]:
        if neighbor != parent:
            stack.append((neighbor, node))

# Process the nodes in post-order (bottom-up)
while postorder_stack:
    node, parent = postorder_stack.pop()
    
    for neighbor in graph[node]:
        if neighbor != parent:
            # Node is white: its children can be either white or black
            dp[node][0] = dp[node][0] * (dp[neighbor][0] + dp[neighbor][1]) % MOD
            # Node is black: its children must be white
            dp[node][1] = dp[node][1] * dp[neighbor][0] % MOD

# The answer is the sum of ways to paint the root node (either white or black)
result = (dp[1][0] + dp[1][1]) % MOD
print(result)
