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



"""
Recursive solution

from collections import defaultdict
N = int(input())
arr = list(map(float, input().split()))
dp = defaultdict(int)
ans = 0
def dfs(ind, H, T):
  # nonlocal ans
  if (ind, H, T) in dp: return dp[(ind, H, T)]
  if ind == N:
    if H > T: return 1
    return 0
  
  head = arr[ind] * dfs(ind + 1, H + 1, T)
  tail = (1- arr[ind]) * dfs(ind + 1, H, T + 1)
  curr = head + tail

  
  dp[(ind, H, T)] = curr
  return curr
  
print(dfs(0,0,0))
  

"""
