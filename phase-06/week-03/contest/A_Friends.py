"""

https://codeforces.com/gym/561419/problem/A

PASSED

"""

from math import ceil

a = int(input())
print("a =", a)

b = int(input())
print("b =", b)

tot = lambda x: x*(x+1)//2

diff = abs(a - b)

c = ceil(diff/2)
d = diff - c
print(tot(c) + tot(d))

