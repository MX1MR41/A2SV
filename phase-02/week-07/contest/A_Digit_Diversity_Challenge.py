"""

https://codeforces.com/gym/502190/problem/A

PASSED
"""

l, r = list(input().split())
a, b = int(l), int(r)

for i in range(a, b+1):
    seen = set()
    j = str(i)
    for c in j:
        if c in seen:
            break
        seen.add(c)

    else:
        print(i)
        break

else:
    print(-1)