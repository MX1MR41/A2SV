# https://atcoder.jp/contests/dp/tasks/dp_n

def min_cost_to_combine_slimes(n, arr):
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    
    dp = [[0] * n for _ in range(n)]
    
    
    for length in range(2, n + 1):  
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            total_sum = prefix_sum[j + 1] - prefix_sum[i]
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + total_sum)
    
    
    return dp[0][n - 1]


n = int(input())
arr = list(map(int, input().split()))


result = min_cost_to_combine_slimes(n, arr)


print(result)
