"""
https://codeforces.com/gym/490001/problem/C

PASSED
"""

n = int(input())

for i in range(n):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        length = len(word)-2
        print(f"{word[0]}{length}{word[-1]}")
