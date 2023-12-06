"""
https://codeforces.com/problemset/problem/1509/A

PASSED
"""

n = int(input())

for i in range(n):
    odd, even = 0, int(input()) - 1
    arr = list(map(int, input().split()))
    while odd < even:
        if arr[odd] % 2 == 1:
            odd += 1
        else:
            arr[odd], arr[even] = arr[even], arr[odd]
            even -= 1

    print(*arr, sep=' ')