"""

https://codeforces.com/gym/524965/problem/A

PASSED
"""

from collections import Counter, defaultdict


n = int(input())

arr = list(map(int, input().split()))

arr = [(j,i+1) for i, j in enumerate(arr)]
arr.sort()
# print(arr)\
ans = []

tot = arr[0] + arr[-1]
i, j = 0, n-1
while i < j:
    temp = (arr[i][1], arr[j][1])
    ans.append(temp)

    i += 1
    j -= 1

for i in ans:
    print(*i)
    