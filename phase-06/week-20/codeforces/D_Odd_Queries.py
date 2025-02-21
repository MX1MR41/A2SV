"""

https://codeforces.com/contest/1807/problem/D

"""

for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i in range(1, n):
        arr[i] += arr[i - 1]

    tot = arr[-1]

    for _ in range(q):
        l, r, k = list(map(int, input().split()))
        l -= 1
        r -= 1
        curr = arr[r] - arr[l - 1] if l > 0 else arr[r]
        new_sum = tot - curr + k*(r - l + 1)

        if new_sum % 2:
            print("YES")
        else:
            print("NO")
