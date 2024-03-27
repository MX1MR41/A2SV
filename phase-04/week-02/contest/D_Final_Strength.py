def mergeSort(arr, l, r):
    if l == r:
        return
    
    mid = (l + r) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    wins = [0] * (r - l + 1)
    merged = []
    ptr = mid + 1
    
    for i in range(l, mid + 1):
        while ptr <= r and arr[ptr][1] < arr[i][1]:
            ptr += 1
        wins[i - l] = ptr - (mid + 1)
    
    ptr = l
    for i in range(mid + 1, r + 1):
        while ptr <= mid and arr[ptr][1] < arr[i][1]:
            ptr += 1
        wins[i - l] = ptr - l
    
    pt1 = l
    pt2 = mid + 1
    
    while pt1 <= mid or pt2 <= r:
        if pt2 > r or (pt1 <= mid and arr[pt1][1] + wins[pt1 - l] < arr[pt2][1] + wins[pt2 - l]):
            arr[pt1][1] += wins[pt1 - l]
            merged.append(arr[pt1])
            pt1 += 1
        else:
            arr[pt2][1] += wins[pt2 - l]
            merged.append(arr[pt2])
            pt2 += 1
    
    arr[l:r + 1] = merged

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [[i, j] for i, j in enumerate(arr)]
    mergeSort(arr, 0, 2 ** n - 1)
    ans = [i[1] for i in sorted(arr, key=lambda x: x[0])]
    print(*ans)

t = int(input())
for _ in range(t):
    solve()
