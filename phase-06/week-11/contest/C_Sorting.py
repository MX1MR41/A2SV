"""

PASSED
"""


n = int(input())
arr = list(map(int, input().split()))

if arr == sorted(arr):
    print("yes")
    print(1, 1)
    exit()

l, r = 0, 0
for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        l = i
        break

for i in range(l, n - 1):
    if arr[i] < arr[i + 1]:
        r = i
        break

if r == 0:
    r = n - 1

arr = arr[:l] + arr[l:r + 1][::-1] + arr[r + 1:]

if arr == sorted(arr):
    print("yes")
    print(l + 1, r + 1)
    
else:
    print("no")
