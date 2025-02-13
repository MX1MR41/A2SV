"""

https://codeforces.com/contest/1343/problem/C

"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    tot = 0
    _max = float("-inf")
    for r in range(n):
        curr = arr[r]
        if _max == float("-inf"):
            _max = curr
        else:
            if curr < 0:
                if _max < 0:
                    _max = max(_max, curr)
                else:
                    tot += _max
                    _max = curr
            else:
                if _max > 0:
                    _max = max(_max, curr)
                else:
                    tot += _max
                    _max = curr

    tot += _max
    print(tot)

