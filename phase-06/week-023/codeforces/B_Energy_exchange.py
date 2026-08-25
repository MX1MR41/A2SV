"""

https://codeforces.com/problemset/problem/68/B

"""

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort(reverse = True)

def check(x):
    extra = 0
    for i in a:
        if i > x:
            extra += i - x - k*(i - x)/100
        elif i < x:
            if i + extra < x:
                return False
            
            extra -= x - i
            
    return True

    
l, r = 0, 10**3
res = 0
while l <= r:
    mid = (l + r)/2
    if check(mid):
        res = mid
        l = mid + 10**(-8)
    else:
        r = mid - 10**(-8)

print(res)
