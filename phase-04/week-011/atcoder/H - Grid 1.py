# https://atcoder.jp/contests/dp/tasks/dp_h
# classic dp enumeration problem

H, W = list(map(int, input().split()))
grid = []
for _ in range(H):
  grid.append(list(input()))
dp = [[0]*W for _ in range(H)]
dp[-1][-1] = 1

for i in reversed(range(H)):
  for j in reversed(range(W)):
    if (i,j) == (H-1, W-1): continue
    
    if grid[i][j] == "#":
      dp[i][j] = 0
      continue
    
    if i == H-1:
      down, right = 0, dp[i][j+1]
    elif j == W-1:
      down, right = dp[i+1][j], 0
      
    else:
      down, right = dp[i+1][j], dp[i][j+1]
      
    dp[i][j] = down + right
    
print(dp[0][0] % (10**9+7))
      
    
