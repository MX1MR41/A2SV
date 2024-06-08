"""

https://codeforces.com/gym/522079/problem/B

PASSED
"""

for _ in range(int(input())):
    n, z = list(map(int, input().split()))
    a = list(map(int, input().split()))
    temp = [i & z for i in a]
    temp.append(z)
    curr = max(temp)
    print(max([i|curr for i in a]))