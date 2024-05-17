"""

https://codeforces.com/gym/515998/problem/C


"""

from sys import stdin


def input(): return stdin.readline().strip()

N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1]*N
color[0] = 0
stack = [0]

cnt = [0]*2

while stack:
    v = stack.pop()
    parent_color = color[v]
    child_color = 1 - parent_color
    cnt[parent_color] += 1

    for ch in adj[v]:
        if color[ch] == -1:
            color[ch] = child_color
            stack.append(ch)

print(cnt[0]*cnt[1] - (N - 1))