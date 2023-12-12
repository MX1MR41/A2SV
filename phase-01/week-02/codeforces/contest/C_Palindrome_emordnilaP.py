"""
https://codeforces.com/gym/491508/problem/C

PASSED
"""

n = int(input())

for _ in range(n):
    l = int(input())
    arr = list(map(int, input().split()))

    flag = False

    for i in range(l-1):
        c = arr.count(arr[i])
        if c >= 2 and arr[i] in arr[i+2:]:
            flag = True






                
    if flag:
        print("YES")
    else:
        print("NO")
