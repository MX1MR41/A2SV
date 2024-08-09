from collections import deque
 
n = int(input())
given_points = set()
points = []

for _ in range(n):
    x, y =  map(int, input().split())
    points.append((x, y))
    given_points.add((x, y))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque()
visited = {}

for x, y in points:
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if (nx, ny) not in given_points:
            visited[(x, y)] = (nx, ny)
            queue.append((x, y))
            break


while queue:

    for _ in range(len(queue)):

        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if (nx, ny) not in visited and (nx, ny) in given_points:
                visited[(nx, ny)] = visited[(x, y)]
                queue.append((nx, ny))

ans = []
for x, y in points:
    ans.append(visited[(x, y)])
for a, b in ans:
    print(a, b)