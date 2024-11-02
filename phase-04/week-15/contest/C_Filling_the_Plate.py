"""

PASSED

"""

from collections import defaultdict, deque


k, m, n = list(map(int, input().split()))
input()



layers = []
for _ in range(k):
    mat = []
    for _ in range(m):
        mat.append(input())
    layers.append(mat)
    input()

# print(*layers, sep = "\n\n")

dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
valid = lambda z, x, y: 0 <= z < k and 0 <= x < m  and 0 <= y < n 

start_x, start_y = list(map(int, input().split()))
# print("start =", x, y)
g = defaultdict(set)

for z in range(k):
    for x in range(m):
        for y in range(n):

            if layers[z][x][y] == ".":

                for d_z, d_x, d_y in dirs:
                    new_z, new_x, new_y = z + d_z, x + d_x, y + d_y
                    if valid(new_z, new_x, new_y) and layers[new_z][new_x][new_y] == ".":
                        g[(z, x, y)].add((new_z, new_x, new_y))
                        g[(new_z, new_x, new_y)].add((z, x, y))

seen = set()
que = deque([(0, start_x -1, start_y - 1)])
tot = 0

while que:
    # print("que now", que)
    for _ in range(len(que)):
        curr = que.popleft()
        if curr in seen:
            continue
        seen.add(curr)
        tot += 1
        for nei in g[curr]:
            if nei not in seen:
                que.append(nei)

print(tot)


