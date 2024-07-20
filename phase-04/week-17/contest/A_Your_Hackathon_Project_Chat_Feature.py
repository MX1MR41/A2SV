"""

https://codeforces.com/gym/534160/problem/A

PASSED
"""

for _ in range(int(input())):
    n = int(input())
    s = input()
    i = n - 1
    while i >= 0 and s[i] == ")":
        i -= 1
    
    if i == -1 or (i + 1 < n - (i + 1)):
        print("Yes")
    else:
        print("No")
