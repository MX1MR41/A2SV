num_stations = int(input())
connections = [[] for _ in range(num_stations)]

for _ in range(num_stations):
    station1, station2 = map(int, input().split())
    connections[station1 - 1].append(station2 - 1)
    connections[station2 - 1].append(station1 - 1)

degree = [len(x) for x in connections]
leaves = [i for i in range(num_stations) if degree[i] == 1]

distance = [0] * num_stations

for leaf in leaves:
    distance[leaf] = num_stations
    for neighbor in connections[leaf]:
        degree[neighbor] -= 1
        if degree[neighbor] == 1:
            leaves.append(neighbor)

leaves.extend(i for i in range(num_stations) if not distance[i])

for leaf in leaves[::-1]:
    for neighbor in connections[leaf]:
        distance[neighbor] = min(distance[neighbor], distance[leaf] + 1)

print(" ".join(map(str, distance)))
