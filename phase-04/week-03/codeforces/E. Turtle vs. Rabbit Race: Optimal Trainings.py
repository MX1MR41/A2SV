def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + arr[i - 1]

    for _ in range(int(input())):
        l, u = map(int, input().split())
        lo, hi = l, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if pre[mid] - pre[l - 1] <= u:
                lo = mid
            else:
                hi = mid - 1
        maxu, res = -1e18, 0
        
        for i in range(max(l, lo - 2), min(n, lo + 2) + 1):
            t = pre[i] - pre[l - 1]
            ut = (u + (u - t + 1)) * t // 2
            if ut > maxu:
                maxu = ut
                res = i
        print(res, end=" ")


for i in range(1, int(input()) + 1):
    solve()
    print()
