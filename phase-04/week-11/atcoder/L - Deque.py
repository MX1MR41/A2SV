# https://atcoder.jp/contests/dp/tasks/dp_l

N = int(input())
arr = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]


for i in range(N):
    dp[i][i] = arr[i]


for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j] = max(arr[i] - dp[i + 1][j], arr[j] - dp[i][j - 1])



print(dp[0][N-1])


