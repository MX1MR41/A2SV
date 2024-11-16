"""

https://codeforces.com/gym/564758/problem/A

PASSED
"""




for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    ops = 0
    while a <= c and b <= c:
        if a <= b:
            a += b
        else:
            b += a

        ops += 1

    print(ops)
    
    