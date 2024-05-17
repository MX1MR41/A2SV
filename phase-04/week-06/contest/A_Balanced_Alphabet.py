"""

https://codeforces.com/gym/520390/problem/A

PASSED
"""

for _ in range(int(input())):
    n, k = list(map(int, input().split()))

    _min = n // k

    s = "" 

    for i in range(k):
        s += chr(97 + i) * _min

    curr = n - len(s)
    s += "a" * curr

    print(s)