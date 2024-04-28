def gcd(a,b):
    if a == b:
        return a
    return 1
 
 
print(gcd(*(list(map(int, input().split())))))
