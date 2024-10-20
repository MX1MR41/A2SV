"""

PASSED

"""

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

mex = 1
for i in range(n):
    if arr[i] >= mex:
        arr[i] = mex
        mex += 1

print(mex)
