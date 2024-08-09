from heapq import heapify, heappop, heappush


n = int(input())
m = int(input())
a = [int(input()) for line in range(n)]

_max = max(a) + m

heapify(a)
for i in range(m):
    min_bench = heappop(a)
    heappush(a, min_bench + 1)

_min = max(a)
print(_min, _max)
