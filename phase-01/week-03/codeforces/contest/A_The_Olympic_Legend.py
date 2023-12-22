"""
https://codeforces.com/gym/493037/problem/A

PASSED
"""
"""

https://codeforces.com/gym/493037/problem/A

PASSED
"""
n = int(input())

for _ in range(n):
    count = 0
    run = list(map(int, input().split()))
    k = run[0]
    for i in run[1:]:
        if i > k:
            count += 1

    print(count)