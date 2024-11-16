"""
PASSED

"""

n, b, d = list(map(int, input().split()))
arr = list(map(int, input().split()))

w = 0
cnt = 0
for i in arr:
    if i <= b:
        w += i

    if w > d:
        w = 0
        cnt += 1

if w > d:
    cnt += 1

print(cnt)
