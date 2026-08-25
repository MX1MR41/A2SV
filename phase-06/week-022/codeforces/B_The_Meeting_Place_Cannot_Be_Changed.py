"""

https://codeforces.com/problemset/problem/780/B

"""


n = int(input())
arr = list(map(int, input().split()))
v = list(map(int, input().split()))

arr = sorted(list(zip(arr, v)))


def check(x):
    right = float("inf")
    left = float("-inf")

    for p, s in arr:
        left = max(left, p - s * x)
        right = min(right, p + s * x)

    return left <= right


l, r = 0, 10**9

res = float("inf")

while l <= r:
    mid = (l + r) / 2

    if check(mid):
        res = mid
        r = mid - 10 ** (-6)

    else:
        l = mid + 10 ** (-6)


print(res)
