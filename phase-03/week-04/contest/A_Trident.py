"""

https://codeforces.com/gym/508328/problem/A

PASSED
"""

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    for j in range(1, n-1):
        if p[j-1] < p[j] and p[j]>p[j+1]:
            print('YES')
            print(j,j+1,j+2)
            break
    else:
        print("NO")