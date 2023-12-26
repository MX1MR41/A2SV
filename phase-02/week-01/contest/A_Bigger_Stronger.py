"""
https://codeforces.com/gym/494181/problem/A

PASSED
"""

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    SET = set()
    same = False

    if n == 1:
        print("YES")
        continue

    for i in arr:
        if i in SET:
            same = True
            print("NO")
            break
        else:
            SET.add(i)

    if not same:
        print("YES")

 