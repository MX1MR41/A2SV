"""

https://codeforces.com/gym/575000/problem/A

PASSED

"""

for _ in range(int(input())):
    x, y, a, b = list(map(int, input().split()))

    t = (y - x)/(a + b)
    if int(t) != t:
        print(-1)
        continue
    print(int(t))

