"""
https://codeforces.com/problemset/problem/2065/C2
"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()  
    valid = True

    maxb = b[-1]
    if maxb - a[-1] > a[-1]:
        a[-1] = maxb - a[-1]
    
    for i in range(n - 2, -1, -1):

        should_be = a[i + 1]
        l, r = 0, m - 1
        res = 0
        while l <= r:
            mid = (l + r)//2
            shift = b[mid]
            if shift - a[i] <= should_be:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        curr = b[res] - a[i] if b[res] - a[i] <= should_be else a[i]
        if a[i] > should_be:
            a[i] = curr
        else:
            a[i] = max(a[i],curr)

    valid = True
    for i in range(n- 1):
        if a[i] > a[i + 1]:
            valid = False
            break

    if valid:
        print("YES")
    else:
        print("NO")

    
            


