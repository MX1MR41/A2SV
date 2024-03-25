"""

https://codeforces.com/gym/504939/problem/B

PASSED
"""

s = input()
stk = []
res = 0
for i in s:
    if i == "(":
        stk.append(i)
    else:
        if stk and stk[-1] == "(":
            res += 2
            stk.pop()
            
print(res)