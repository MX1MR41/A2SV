"""

https://codeforces.com/gym/494181/problem/B

PASSED
"""
from collections import defaultdict
t = int(input())

db = defaultdict(int)

for _ in range(t):

    s = input()

    if db[s]:
        out = s + str(db[s])
        db[s] += 1
        print(out)

    else:
        print("OK")
        db[s] += 1


