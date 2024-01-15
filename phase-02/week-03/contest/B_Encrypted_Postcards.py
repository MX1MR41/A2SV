"""

https://codeforces.com/gym/496610/problem/B

PASSED
"""

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    p = s[0]
    r = s[0]
    i = 1

    while i < n:
        if s[i] == p:
            i += 1
            if i < n:
                p = s[i]
                r += p
        i += 1

    print(r)

    