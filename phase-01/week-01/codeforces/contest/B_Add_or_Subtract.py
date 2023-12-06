"""
https://codeforces.com/gym/490001/problem/B

PASSED
"""

n = int(input())

for i in range(n):
    a, b , c = map(int, input().split())
    if a + b == c:
        print("+")
    else: 
        print("-")