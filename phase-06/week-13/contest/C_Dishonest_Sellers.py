"""

PASSED

"""

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [(i, j) for i, j in zip(a,b)]

c.sort(key = lambda x: x[0] - x[1])
# print(c)
tot = sum(i[0] for i in c[:k])
for i in range(k, n):
    tot += min(c[i])

print(tot)