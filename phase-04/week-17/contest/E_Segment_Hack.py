import sys
from collections import defaultdict
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

q = int(input())

segments = defaultdict(int)
max_heap = []
min_heap = []

for _ in range(q):
    operation, l, r = input().split()
    l, r = int(l), int(r)

    if operation == '+':
        heappush(max_heap, (-l, r))
        heappush(min_heap, (r, l))
        segments[(l, r)] += 1
    else:
        segments[(l, r)] -= 1

    while max_heap:
            neg_left, right = max_heap[0]
            if segments[(-neg_left, right)]:
                break

            else:
                heappop(max_heap)
    
    while min_heap:
        right, left = min_heap[0]
        if segments[(left, right)]:
            break

        else:
            heappop(min_heap)

    if max_heap and min_heap and -max_heap[0][0] > min_heap[0][0]:
        print('YES')
    else:
        print('NO')