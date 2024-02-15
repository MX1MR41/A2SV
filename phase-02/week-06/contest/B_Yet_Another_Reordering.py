t = int(input())
arr = list(map(int, input().split()))
arr.sort()
l = 0

for r in range(t):
    
    if arr[l] < arr[r]:
        l += 1
       
print(l)