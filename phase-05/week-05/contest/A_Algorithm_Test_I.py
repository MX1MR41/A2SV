"""

https://codeforces.com/gym/546592/problem/A

PASSED
"""

from math import factorial

m = int(input())
a = len(set(list(map(int, input().split()))))

print(factorial(a))