# https://codeforces.com/contest/1996/problem/E

# diff[i] = ones[i] - zeros[i]
# for each diff, you must find previous same diffs because erasing those diffs will make the substring valid
# since we will be calculating diff[i]*diff[i - x] + diff[i]*diff[i - y] = diff[i]*(diff[i - x], diff[i - y]), assuming diff[i] == diff[i - x] == diff[i - y]
# we can accumulate diff[i - y] and diff[i - x] in a dictionary, then use it for diff[i]

from collections import defaultdict

mod = 10**9 + 7
for _ in range(int(input())):
    s = input()
    zeros = []
    ones = []
    z = o = 0

    for i in range(len(s)):
        if s[i] == "0":
            z += 1
        else:
            o += 1

        zeros.append(z)
        ones.append(o)


    res = 0
    n = len(s)
    tot = defaultdict(int)
    arr = []
    tot[0] = 1
    for i in range(n):
        arr.append(ones[i] - zeros[i])
        curr = ones[i] - zeros[i]
        res = (res + (n - i) * tot[curr]) % mod
        tot[curr] += i + 2

    print(res % mod)

 
