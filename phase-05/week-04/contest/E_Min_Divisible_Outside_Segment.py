"""

https://codeforces.com/gym/545013/problem/E

PASSED

"""


for _ in range(int(input())):
    l, r, d = list(map(int, input().split()))
    if l > d:
        ans = d
    else:
        ans = (r//d + 1)*d
    print(ans)


