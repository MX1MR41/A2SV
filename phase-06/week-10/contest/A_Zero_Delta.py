"""

https://codeforces.com/gym/573555/problem/A

PASSED

"""

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    l, r = 0, n - 1

    while l < r and k:
        if arr[l]:
            arr[l] -= 1
            arr[r] += 1

            k -= 1
        else:
            l += 1


    print(*arr)
        