"""

PASSED

"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = []
    n = len(arr)
    if n % 2:
        mid = n//2
        ans.append(arr[mid])
        l, r = mid -1, mid + 1

    else:
        l, r = n//2 - 1, n//2

    # print(l, r)

    while l >= 0 and r < n:
        ans.append(min(arr[l], arr[r]))
        ans.append(max(arr[l], arr[r]))
        l -= 1
        r += 1

    print(*ans)