from collections import defaultdict


n, q = list(map(int, input().split()))
ends = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    ends.append(x * y)


for i in range(1, len(ends)):
    ends[i] += ends[i - 1]

# print(ends)

qs = list(map(int, input().split()))


res = []

for m in qs:
    ind = 0
    l, r = 0, len(ends) - 1

    while l <= r:
        mid = (l + r)//2
        if ends[mid] >= m:
            ind = mid + 1

            r = mid - 1
        else:
            l = mid + 1

    res.append(ind)


print(*res, sep = "\n")


