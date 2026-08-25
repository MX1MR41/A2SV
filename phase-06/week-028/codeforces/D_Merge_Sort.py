# https://codeforces.com/problemset/problem/873/D

n, k = list(map(int, input().split()))
if k % 2 == 0:
    print(-1)
    exit(0) 

k -= 1
arr = [i for i in range(1, n + 1)]

def dfs(l, r, arr):
    global k
    if r - l <= 1 or k <= 0:
        return 
    
    mid = (l + r) // 2
    arr[mid - 1], arr[mid] = arr[mid], arr[mid - 1]
    k -= 2
    
    if k > 0:
        dfs(l, mid, arr)
    
    if k > 0:
        dfs(mid, r, arr)

dfs(0, n, arr)

if k == 0:
    print(*arr)
else:
    print(-1)

    
    
    



