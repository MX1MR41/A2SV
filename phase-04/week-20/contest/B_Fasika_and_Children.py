"""

PASSED
"""
from collections import deque

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr = [(i, ind + 1) for ind, i in enumerate(arr)]
que = deque(arr)

last = None
while que:
    if len(que) == 1:
        break

    ch, ind = que.popleft()
    if ch - m > 0:
        que.append((ch - m, ind))


last, ind = que.popleft()
print(ind)
