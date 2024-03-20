"""

https://codeforces.com/gym/511242/problem/A

PASSED
"""

for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    num = input()
    flag = False
    res = ""
    for i in range(n):
        if num[i] < str(d):
            res = num[:i] + str(d) + num[i:]
            flag = True
            break

    if not flag: res = num + str(d)

    print(res)
        
