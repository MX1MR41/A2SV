"""

PASSED
"""


def p(x, k):
    ans = 0
    for i in range(2, int(x**(1/2)) + 1):
        if not x % i:
            d = x / i
            if d <= k:
                ans = max(d, ans)
            if i <= k:
                ans = max(ans, i)

    return ans


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if k == 1:
        print(n)
        continue
    if k >= n:
        print(1)
        continue
    y = int(p(n, k))
    if not y:
        print(n)
        continue


    print(n//y)







    