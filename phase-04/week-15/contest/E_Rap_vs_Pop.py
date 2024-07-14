import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")


for _ in range(int(input())):
   n = int(input())
   g = [[0] * n for _ in range(n)]
   a = [input().split() for _ in range(n)]


   for i in range(n):
       for j in range(i):
           if a[i][0] == a[j][0] or a[i][1] == a[j][1]:
               g[i][j] = g[j][i] = 1
  
   dp = [[0] * n for _ in range(1 << n)]


   for i in range(n):
       dp[1 << i][i] = 1


   ans = 1


   for i in range(1, 1 << n):
       for j in range(n):
           if dp[i][j]:
               takes = bin(i).count('1')
               ans = max(ans, takes)
               for k in range(n):
                   if i & (1 << k) == 0 and g[j][k] == 1:
                       dp[i | 1 << k][k] = 1
  
   print(n - ans)