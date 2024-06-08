"""

https://codeforces.com/gym/526229/problem/A

PASSED
"""

n = int(input())
arr = list(map(int, input().split()))
ans = 1

l  = 0
last = arr[0]
for r in range(1, n):
    if arr[r] <= last:
        l = r 
    last = arr[r] 

    ans = max(ans, r - l + 1)

print(ans)