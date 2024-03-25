"""

https://codeforces.com/gym/506437/problem/C

PASSED
"""

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    stk = []
    res = 0
    for i in a:
        flag = False
        while stk and stk[-1] > i:
            flag = True
            stk.pop()
            res += 1

        stk.append(i)

    print(res)