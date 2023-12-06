"""
https://codeforces.com/gym/490001/problem/D

PASSED
"""

n = int(input())

total = 0
arr = list(map(int, input().split()))

tmp = sum(arr)
if tmp % 2 == 0:
    total += tmp
    print(total)
else:
    arr.sort()
    for i in range(n):
        if arr[i] % 2 != 0:
            # arr.pop(i)
            tmp -= arr[i]
        if tmp % 2 == 0:
            total = tmp
            print(total)
            break 
