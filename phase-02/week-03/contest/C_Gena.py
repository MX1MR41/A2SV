"""

https://codeforces.com/gym/496610/problem/C


PASSED
"""

m = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
n = int(input())
arr2 = list(map(int, input().split()))
arr2.sort()
i , j = 0, 0
ans = 0

while i < m and j < n:
    p, q = arr1[i], arr2[j]
    d = abs(p - q)
    if d <= 1:
        ans += 1
        i += 1
        j += 1
    else:
        if q > p:
            i += 1
        else:
            j += 1

print(ans)