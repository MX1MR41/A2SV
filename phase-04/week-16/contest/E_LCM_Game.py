from math import lcm

N = int(input())

ans = 0
if N >= 3:
    ans = lcm(N, N - 1, N - 2)

if N >= 4:
    ans = lcm(N - 1, N - 2, N - 3)

min_n = max(1, N - 50)
for i in range(min_n, N + 1):
    for j in range(min_n, N + 1):
        for k in range(min_n, N + 1):
            ans = max(ans, lcm(i, j, k))
print(ans)