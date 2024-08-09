"""

https://codeforces.com/gym/538762/problem/A

PASSED
"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    odd = even = 0
    for i in arr:
        if i % 2:
            odd += 1
        else:
            even += 1

    if even == odd:
        print("Yes")
    else:
        print("No")