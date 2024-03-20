"""

https://codeforces.com/gym/511242/problem/B

PASSED
"""

from bisect import *

n = int(input())
worms = list(map(int, input().split()))
t = int(input())
ws = list(map(int, input().split()))

inters = []
temp = 0
for i in worms:
    inters.append([temp+1, temp+i])
    temp = temp + i


ends = [i[1] for i in inters]
for w in ws:
    s = bisect_left(ends, w)
    if s == n or inters[s][1] < w:
        s -= 1
    print(s+1)
    
