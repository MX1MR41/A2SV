"""

https://codeforces.com/gym/522079/problem/E

"""

import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    s = sys.stdin.readline().strip()
    q = int(sys.stdin.readline().strip())

    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] ^ a[i-1]

    x_0 = 0
    x_1 = 0
    for i in range(n):
        if s[i] == "0":
            x_0 ^= a[i]
        else:
            x_1 ^= a[i]

    ans = []
    for i in range(q):
        line = list(map(int, sys.stdin.readline().strip().split()))
        if line[0] == 2:
            if line[1]:
                ans.append(int(str(x_1)))
            else:
                ans.append(int(str(x_0)))
        else:
            l, r = line[1], line[2]
            seg = pref[r] ^ pref[l - 1]   
            x_0 ^= seg
            x_1 ^= seg
    print(*ans)