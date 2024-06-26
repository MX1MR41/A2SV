"""

https://codeforces.com/gym/530187/problem/A

PASSED

"""

n = int(input())
s = input()

i = 0
skip = 1
ans = ""
while i < n:
    ans += s[i]
    i += skip
    skip += 1

print(ans)