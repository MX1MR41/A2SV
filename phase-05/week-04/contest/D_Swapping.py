"""

https://codeforces.com/gym/544853/problem/D

PASSED
"""

for _ in range(int(input())):
    n, x, m = list(map(int, input().split()))
    _min = _max = x
    flag = False
    for _ in range(m):
        l, r = list(map(int, input().split()))

        if (l <= _min and r >= _min) or (r >= _max and l <= _max):
            _min = min(l, _min)
            _max = max(r, _max)



    print(_max + 1 - _min)





