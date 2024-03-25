"""

https://codeforces.com/gym/506437/problem/B

PASSED
"""

s = input()
stk = []
for i in s:
    flag = False
    if stk and stk[-1] == i:
        stk.pop()
        flag = True

    if not flag:
        stk.append(i)

print("".join(stk))