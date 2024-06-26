import heapq

n = int(input())
a = list(map(int, input().split()))

h = []
total_sum = 0

for potion in a:
    total_sum += potion
    heapq.heappush(h, potion)
    while total_sum < 0:
        total_sum -= heapq.heappop(h)

print(len(h))