"""

https://codeforces.com/gym/532814/problem/A

PASSED
"""

from collections import Counter
n, k = list(map(int, input().split()))
s = input()
for i in range(k):
    if chr(65 + i) not in s:
        print(0)
        exit()

cnt = Counter(s)
res = n
for i in range(k):
    res = min(res, cnt[chr(65 + i)])

print(res*k)


    
