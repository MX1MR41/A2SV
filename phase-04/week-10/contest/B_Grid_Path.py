"""

https://codeforces.com/gym/524965/problem/B

PASSED
"""

for _ in range(int(input())):
    m, n, k = list(map(int, input().split()))

    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 0
    for i in range(m):
        for j in range(n):
            if (i,j) == (0,0): continue
            if j == 0:
                left = float("inf")
                up = dp[i-1][j]
            elif i == 0:
                up = float("inf")
                left = dp[i][j-1]

            else:
                up, left = dp[i-1][j], dp[i][j-1]

            dp[i][j] = min(i+1 + left, j+1 + up)

    # print(dp)
    # print("-"*100)
    if dp[-1][-1] == k: print("YES")
    else: print("NO")

