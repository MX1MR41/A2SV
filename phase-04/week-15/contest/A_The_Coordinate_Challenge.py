"""

https://codeforces.com/gym/531455/problem/A

"""

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(2)
        continue

    ans = n // 3
    if n % 3:
        ans += 1

    print(ans)