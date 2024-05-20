# https://atcoder.jp/contests/dp/tasks/dp_b

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

dp = [float("inf")] * n
dp[0] = 0

dp[1] = abs(arr[0] - arr[1])

for i in range(2, n):
  for j in range(1, min(i+1, k+1 )):
    dp[i] = min(dp[i], dp[i-j] + abs(arr[i] - arr[i-j]))
  
print(dp[-1])
