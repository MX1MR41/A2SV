"""

https://codeforces.com/gym/533460/problem/A

PASSED
"""

for _ in range(int(input())):
    s = input()
    
    num = int(s[0])
    res = 0
    res += 10*(num-1)
    if len(s) == 1:
        res += 1
    elif len(s) == 2:
        res += 3
    elif len(s) == 3:
        res += 6
    else:
        res += 10

    print(res)
    