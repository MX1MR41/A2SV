MOD = 10**9 + 7

N, K = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (K + 1)
dp[0] = 1

for i in range(N):
    new_dp = [0] * (K + 1)
    prefix_sum = [0] * (K + 2)
    
    for j in range(K + 1):
        prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MOD
    
    for j in range(K + 1):
        minimum = j - arr[i]
        minimum = max(minimum, 0)
        new_dp[j] = (prefix_sum[j + 1] - prefix_sum[minimum]) % MOD
    
    dp = new_dp

print(dp[K] % MOD)











"""
# SPACE UNOPTIMIZED VERSION N^2
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
  
    pre_sum_dp = [0] * (K + 2)
    for j in range(K + 1):
        pre_sum_dp[j + 1] = (pre_sum_dp[j] + dp[i][j])

    for j in range(K + 1):
        minimum = max(0, j - a[i])
        dp[i + 1][j] = (pre_sum_dp[j + 1] - pre_sum_dp[minimum])
        # pre_sum_dp[j + 1] is the sum of dp[i][0] to dp[i][j].
        # pre_sum_dp[minimum] is the sum of dp[i][0] to dp[i][minimum-1].
        
        
UNOPTIMIZED VERSION N^3        

dp = [[0]*(K+1) for _ in range(N)]

for i in range(N):
  dp[i][0] = 1

for i in range(1, arr[0]+1):
  dp[0][i] = 1
  
for i in range(1, N):
  for j in range(1, K+1):
    curr = 0
    for q in range(arr[i]+1):
      curr += dp[i-1][j-q]
    dp[i][j] = curr % (10**9 + 7)

"""
