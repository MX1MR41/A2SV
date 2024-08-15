"""
https://codeforces.com/gym/541681/problem/A

PASSED
"""

for _ in range(int(input())):
    key = input()
    s = input()
    tot = 0
    val = {l : (i+1) for i, l in enumerate(key)}
    for i in range(len(s) - 1):
        tot += abs(val[s[i]] - val[s[i+1]])

    print(tot)
