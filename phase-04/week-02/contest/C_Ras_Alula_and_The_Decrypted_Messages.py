"""

https://codeforces.com/gym/513152/problem/C

PASSED
"""

for _ in range(int(input())):
    m, n = list(map(int, input().split()))
    word = input()
    s = input()
    if n > m:
        print("NO")
        continue

    tot = sum([ord(i) for i in s])

    wind = sum([ord(i) for i in word[:n]])

    if wind == tot:
        print("YES")
        continue

    flag = False
    for r in range(n, m):
        wind -= ord(word[r-n])
        wind += ord(word[r])
        if wind == tot:
            flag = True
            break

    if flag: print("YES")
    else: print("NO")

    