"""

https://codeforces.com/gym/497696/problem/C

PASSED
"""

n , k = list(map(int, input().split()))
arr = input()

ans = 0
a = b = 0
l = r = 0

while r < n:

    if arr[r] == "a":
        a += 1

    while a > k:
        
        if arr[l] == "a":
            a -= 1
            
        l += 1

    ans = max(ans, r-l + 1)
    r += 1

l = r = 0
while r < n:

    if arr[r] == "b":
        b += 1

    while b > k:
        
        if arr[l] == "b":
            b -= 1
            
        l += 1

    ans = max(ans, r-l + 1)
    r += 1

print(ans)