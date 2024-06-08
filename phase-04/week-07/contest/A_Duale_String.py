"""

https://codeforces.com/gym/520688/problem/A

PASSED

"""

for _ in range(int(input())):
    s = input()
    n = len(s)
    if n % 2:
        print("NO")
        continue

    mid = n // 2
    if s[:mid] == s[mid:]:
        print("YES")
    else:
        print("NO")
