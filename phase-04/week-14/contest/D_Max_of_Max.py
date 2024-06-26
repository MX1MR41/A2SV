import sys

input = lambda: sys.stdin.readline().rstrip()


def check(max_val):

    # consider each index if it can be where we can achieve this 'max_val'
    for i in range(n):

        cost = 0
        cur_val = max_val
        for j in range(i, n):

            # if it is the last index and in needs to be incremented
            # we are not allowed to increase the last number
            # we can get away by making cost = k + 1, it will not return True
            if a[j] < cur_val and j == n - 1:
                cost = k + 1
                break

            if a[j] >= cur_val:
                break

            cost += cur_val - a[j]
            next_val = max(cur_val - 1, 0)
            cur_val = next_val

        if cost <= k:
            return True

    return False


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    low = max(a)
    high = max(a) + min(k, n)

    while low <= high:

        mid = low + (high - low) // 2

        if check(mid):
            low = mid + 1

        else:
            high = mid - 1

    print(high)
