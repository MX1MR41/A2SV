"""

PASSED

"""

for _ in range(int(input())):
    n = int(input())
    dp = [float("inf")]*(n+2)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(n):

        curr = dp[i]
        m = 1
        nxt = i + 5*m
        while nxt <= n:
            dp[nxt] = min(dp[nxt], curr)
            m += 1
            nxt = i + 5*m

        m = 1
        nxt = i + 3*m
        while nxt <= n:
            dp[nxt] = min(dp[nxt], curr)
            m += 1
            nxt = i + 3*m

        m = 1
        nxt = i + 1*m
        while nxt <= n:
            dp[nxt] = min(dp[nxt], curr + m)
            m += 1
            nxt = i + 1*m
        

    print(dp[n])

        