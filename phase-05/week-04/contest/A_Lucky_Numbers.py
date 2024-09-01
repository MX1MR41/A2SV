"""

PASSED

https://codeforces.com/gym/545013/problem/A
"""

from collections import Counter 

n, k = list(map(int, input().split()))
arr = list(input().split())
ans = 0
for a in arr:
    cnt = Counter(a)
    tot = cnt["4"] + cnt["7"]
    if tot <= k:
        ans += 1

print(ans)

