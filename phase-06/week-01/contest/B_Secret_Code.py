"""

PASSED
"""

n = int(input())
s = input()

ans = ""


l = r = False
if n % 2: r = True
else: l = True

for i in s:
    if r:
        ans += i
    else:
        ans = i + ans

    r = not r
    l = not l

print(ans)


