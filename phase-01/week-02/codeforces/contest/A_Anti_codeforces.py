"""
https://codeforces.com/gym/491508/problem/A

PASSED
"""

n = int(input())
s = "codeforces"
for i in range(n):
    s2 = input()
    cnt = 0
    for i in range(len(s2)):
        if s2[i] != s[i]:
            cnt += 1

    print(cnt)