"""

PASSED

"""

n, k = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
z = 0
_max = [0, 0, 0]  

for r in range(n):
    if arr[r] == 0:
        z += 1

    while z > k:
        if arr[l] == 0:
            z -= 1
        l += 1

    
    curr = r - l + 1
    if curr > _max[0]:  
        _max = [curr, l, r]


if _max[0] > 0:
    l, r = _max[1], _max[2]
    for i in range(l, r + 1):
        arr[i] = 1

print(_max[0])  
print(*arr)  
