"""
https://codeforces.com/gym/517685/problem/D


"""

from collections import deque
from sys import stdin

def input(): 
    return stdin.readline().strip()

N = int(input())
start_x, start_y = map(int, input().split())
target_x, target_y = map(int, input().split())

start_x -= 1
start_y -= 1
target_x -= 1
target_y -= 1

grid = []
for _ in range(N):
    grid.append(input())

visited = [[[False, False] for _ in range(N)] for _ in range(N)]

queue = deque([(start_x, start_y, 1, 1), (start_x, start_y, -1, 1)])

moves = 0
while queue:
    queue_length = len(queue)
    for _ in range(queue_length):
        x, y, dx, dy = queue.popleft()
        if x == target_x and y == target_y:
            print(moves)
            exit()
        visited[x][y][0] = visited[x][y][1] = True
        is_diagonal = (dx == dy)
        
        for direction in [1, -1]:
            for i in range(1, 2 * N):
                nx = x + i * dx * direction
                ny = y + i * dy * direction
                if nx < 0 or nx >= N or ny < 0 or ny >= N or grid[nx][ny] == '#' or visited[nx][ny][is_diagonal]:
                    break
                if not visited[nx][ny][0] and not visited[nx][ny][1]:
                    queue.append((nx, ny, -dx, dy))
                visited[nx][ny][is_diagonal] = True
    moves += 1
print(-1)
