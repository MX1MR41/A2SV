# https://atcoder.jp/contests/dp/tasks/dp_i

N = int(input())
arr = list(map(float, input().split()))
# dp[i][j] = probability of getting j heads after i coin tosses
dp = [[0.0 for _ in range(N+1)] for _ in range(N+1)]


dp[0][0] = 1.0


for i in range(1, N+1):
    for j in range(i+1):  
        if j > 0:
            dp[i][j] += dp[i-1][j-1] * arr[i-1]  
        dp[i][j] += dp[i-1][j] * (1 - arr[i-1])  


ans = 0.0
for j in range((N//2)+1, N+1): # heads > tails 
    ans += dp[N][j]

print(ans)
