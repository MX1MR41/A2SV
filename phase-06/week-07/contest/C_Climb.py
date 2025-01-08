"""


PASSED

"""


n, m = list(map(int, input().split()))

if m > n:
    print(-1)
    exit()

if m == n:
    print(m)
    exit()

_max = n
_min = n//2 + n % 2

# print(_min, _max)


def valid(x):
    l, r = 0, x
    while l <= r:
        mid = (l + r) // 2
        curr = 2*mid + x - mid
        if curr == n:
            return True
        if curr < n:
            l = mid + 1
        else:
            r = mid - 1

    
found = False

for i in range(_min, _max + 1):
    if i % m:
        continue

    if valid(i):
        found = True
        res = i

        break

if found:
    print(res)
else:
    print(-1)

