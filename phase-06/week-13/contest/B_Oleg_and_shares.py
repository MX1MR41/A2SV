"""

PASSED

"""

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
base = min(arr)
tot = 0
for i in arr:
    need = (i - base)/k
    if need != int(need):
        print(-1)
        exit()
    tot += need

print(int(tot))
