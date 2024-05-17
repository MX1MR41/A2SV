"""

https://codeforces.com/gym/519135/problem/C

"""

import sys
from heapq import heappush, heappop

t = int(sys.stdin.readline().strip())

for _ in range(t):
    
    n =  int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    my_heap = []
    ans = 0
    for num in nums:
        if num:
            heappush(my_heap, -1 * num)
        else:
            if my_heap:
                ans +=( heappop(my_heap) * -1)
    print(ans)