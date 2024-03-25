"""

https://codeforces.com/gym/504939/problem/A

PASSED
"""

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    print(max(arr)-min(arr))