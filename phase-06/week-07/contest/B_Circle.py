"""


PASSED

"""

n = int(input())
arr = list(map(int, input().split()))
res = [abs(arr[0] - arr[1]), 0, 1]

for i in range(1, n):
    curr = abs(arr[i] - arr[i-1])
    if curr < res[0]:
        res = [curr, i-1, i]

if abs(arr[0] - arr[-1]) < res[0]:
    res = [abs(arr[0] - arr[-1]), 0, n - 1]

res[1] += 1
res[2] += 1 
print(*res[1:])