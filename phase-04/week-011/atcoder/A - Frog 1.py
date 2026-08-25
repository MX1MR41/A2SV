# https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

dp[1] = abs(arr[0] - arr[1])

for i in range(2, n):
  dp[i] = min(dp[i-1] + abs(arr[i] - arr[i-1]), dp[i-2] + abs(arr[i] - arr[i-2]))
  
print(dp[-1])
