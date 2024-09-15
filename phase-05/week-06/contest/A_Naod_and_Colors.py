"""
https://codeforces.com/gym/548121/problem/A

PASSED
"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 1
    l = 0
    for r in range(n):
        if arr[r] != arr[l]:
            l = r

        ans = max(ans, r - l + 1)

    print(ans)