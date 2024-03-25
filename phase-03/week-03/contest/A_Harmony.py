"""

https://codeforces.com/gym/506437/problem/A

PASSED
"""

t = int(input())
for _ in range(t):
    n, x = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort(reverse = True)

    for i in range(n):
        if a[i] + b[i] > x:
            print("No")
            break
    else: print("Yes")

    if _ != t-1:
        tmp = input()