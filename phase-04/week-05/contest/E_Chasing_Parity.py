"""
https://codeforces.com/gym/517685/problem/E

"""

import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

graph = defaultdict(list)

for i in range(n):
    left, right =  i - arr[i], i + arr[i]
    if left > -1:
        graph[left].append(i)
    if right < n:
        graph[right].append(i)
    
def bfs(start, _end):
    _value = [-1] * n
    queue = deque()
    for num in start:
        queue.append(num)
        _value[num] = 0
    while queue:
        cur = queue.popleft()
        for to in graph[cur]:
            if _value[to] == -1:
                _value[to] = _value[cur] + 1
                queue.append(to)
    for num in _end:
        ans[num] = _value[num]

odd = []
even = []

for i, num in enumerate(arr):
    if num % 2:
        odd.append(i)
    else:
        even.append(i)

ans = [-1] * n

bfs(odd, even)
bfs(even, odd)
print(*ans)
   
    