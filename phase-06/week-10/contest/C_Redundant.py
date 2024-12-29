"""

PASSED

"""

s = input()
def check(size):
    
    for i in range(len(s) - size + 1):
        curr = s[i:i + size]
        for j in range(i + 1, len(s)):
            if s[j:j + size] == curr:
                return True
            
    return False




l, r = 0, len(s)
ans = 0
while l <= r:
    mid = (l + r)//2
    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)


