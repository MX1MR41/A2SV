def solve():

    n, h = map(int, input().split())
    a = list(map(int, input().split()))

    def checker(k):
        cur = k
        for i in range(n - 1):
            cur += min(k, a[i + 1] - a[i])
        return cur >= h
    
    low = 1
    high = h

    while low <= high:

        mid = (low + high)//2

        if checker(mid):
            high = mid - 1
        else:
            low = mid + 1
            
    return low
    
t = int(input())  
for _ in range(t):
    print(solve())