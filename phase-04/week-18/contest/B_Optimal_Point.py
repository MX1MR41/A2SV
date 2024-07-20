for _ in range(int(input())):
    n, k = map(int, input().split())
    
    left = right = False
    for _ in range(n):
        l, r = map(int, input().split())
        
        if l == k:
            left = True
        if r == k:
            right = True
    
    if left and right:
        print("YES")
    else:
        print("NO")