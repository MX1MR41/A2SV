"""
https://codeforces.com/gym/490001/problem/A

PASSED
"""

n = int(input())

string = "codeforces"

for i in range(n):
    c = input()
    if c in string:
        print("YES")
    else:
        print("NO")