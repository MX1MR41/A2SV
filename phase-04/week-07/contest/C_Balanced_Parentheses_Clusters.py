"""

https://codeforces.com/gym/520688/problem/C

PASSED

"""

for _ in range(int(input())):
    n = int(input())
    arr = input()
    ans = 1
    for i in range(1, 2 * n):
        if arr[i] == "(" and arr[i - 1] == "(":
            ans += 1

    print(ans)
