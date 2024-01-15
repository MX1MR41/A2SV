"""

https://codeforces.com/gym/496610/problem/E

"""

from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))


    last_indx = defaultdict(lambda :-1) # stores the last occurence of a given number
    max_dist = defaultdict(int) # stores maximum distance between instances of a given number
    ans = [float('inf')]*n

    # calculate the minimum size segment so that a number can be found in all such segments
    # and take the minimum of those numbers for the segment size
    for indx, num in enumerate(a):
        prev = last_indx[num]
        max_dist[num] = max(max_dist[num], indx - prev)
        
        min_segment_covered = max(max_dist[num], n - indx) - 1
        ans[min_segment_covered] = min(ans[min_segment_covered], num)
        last_indx[num] = indx
    
    # minimum number propagation to larger segment sizes
    for indx in range(1, n):
        ans[indx] = min(ans[indx], ans[indx - 1])
    
    # replace the inf's by -1
    for indx in range(n):
        if ans[indx] == float('inf'):
            ans[indx] = -1
    
    print(*ans)