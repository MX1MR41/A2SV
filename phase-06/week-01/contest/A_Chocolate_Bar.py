"""

https://codeforces.com/gym/557458/problem/A

PASSED
"""

for _ in range(int(input())):
    n, l, r, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    ans = 0

    arr.sort()

    a = 0
    while a < n and arr[a] < l:
        a += 1


    while a < n and arr[a] <= r and k > 0:
        k -= arr[a]
        if k >= 0:
            ans += 1

        a += 1

    print(ans)