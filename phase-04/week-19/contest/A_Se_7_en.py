"""

https://codeforces.com/gym/537362/problem/A
"""

for _ in range(int(input())):
    n = int(input())

    if n % 7 == 0:
        print(n)
    else:
        n -= n % 10
        while n % 7:
            n += 1
        print(n)
