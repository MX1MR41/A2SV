from collections import deque

n, m, k = map(int, input().split())
if k % 2:
    print("IMPOSSIBLE")
    exit(0)

maze = []
direc = {  (1, 0): 'D', (0, -1): 'L', (0, 1): 'R', (-1, 0): 'U' }
src = None 
for i in range(n):
    maze.append(input())
    for j in range(m):
        if maze[i][j] == 'X':
            src = (i, j)
            break
        
#bfs
track = [[float('inf') for _ in range(m)] for _ in range(n)]
track[src[0]][src[1]] = 0
queue = deque([(src, 0)])
visited = set([src])
while queue:
    loc, step = queue.popleft()
    for dx, dy in direc:
        x, y = loc[0] + dx, loc[1] + dy
        if 0 <= x < n and 0 <= y < m and maze[x][y] != '*' and (x, y) not in visited:
            track[x][y] = min(track[x][y], step + 1)
            queue.append(((x, y), step + 1))
            visited.add((x, y))

#dfs
stack = [src]
ans = []
while stack:
    loc = stack.pop()
    if len(ans) == k:
        print("".join(ans))
        exit(0)
    for dx, dy in direc:
        x, y = loc[0] + dx, loc[1] + dy
        if 0 <= x < n and 0 <= y < m and track[x][y] <= k - len(ans):

            ans.append(direc[(dx, dy)])
            stack.append((x, y))
            break

print("IMPOSSIBLE")