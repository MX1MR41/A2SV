"""

https://codeforces.com/gym/503628/problem/D

PASSED
"""

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    total_sum = 0
    for num in a:
        total_sum += num
        if total_sum <= 0:
            return False
    total_sum = 0
    for i in range(n - 1, -1, -1):
        total_sum += a[i]
        if total_sum <= 0:
            return False
    return True

T = int(input())
for _ in range(T):
    if solve():
        print("YES")
    else:
        print("NO")