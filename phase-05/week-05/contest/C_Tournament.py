for _ in range(int(input())):
   n,k =  list(map(int,input().split()))
   arr = list(map(int,input().split()))
   dp = [[0 for _ in range(15)] for _ in range(n+1)]
  
  
   for i in range(1,n+1):
       dp[i][0] = dp[i-1][0]+ arr[i-1]- k
  
       for j in range(1,min(15,i+1)):
  
           dont_div = (dp[i-1][j]+ (arr[i-1]//(2**j))-k)
           div = (dp[i-1][j-1] + arr[i-1]//(2**j))
           dp[i][j] = max(dont_div,div)
  
  
   print(max(dp[n] + [i[-1] for i in dp]))
