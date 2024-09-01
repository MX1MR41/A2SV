"""

https://codeforces.com/gym/543431/problem/A

PASSED
"""

n = int(input())
arr = list(map(int, input().split()))


ans = [arr[-1]]
last = arr[-1]
arr.pop()
for _ in range(n-1):
    curr = arr.pop()
    x = curr + last
    ans.append(x)
    # print("curr", curr, "x", x, "last", last)

    last = curr

print(*ans[::-1])

