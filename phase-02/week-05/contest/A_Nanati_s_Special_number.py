"""

https://codeforces.com/gym/499338/problem/A

PASSED
"""

d = {chr(i): i for i in range(97, 123)}
t = int(input())

for _ in range(t):
    m = 0
    n = int(input())
    s = input()
    for i in s:
        m = max(m, d[i]-96)

    print(m)