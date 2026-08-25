# https://atcoder.jp/contests/dp/tasks/dp_c

N = int(input())
matrix = []
for _ in range(N):
  matrix.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N)]

for j in range(3):
  dp[0][j] = matrix[0][j]

for i in range(1, N):
  for j in range(3):
    dp[i][j] = max(dp[i-1][c] for c in range(3) if c != j) + matrix[i][j]
    
print(max(dp[-1]))

        
