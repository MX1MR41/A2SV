"""

PASSED

"""

from collections import Counter

s = input()
m = int(input())
n = len(s)

if m > n:
    print("impossible")
    exit() 

cnt = Counter(s)

if m <= len(cnt):
    print(0)
    exit()
    
print(m - len(cnt))

