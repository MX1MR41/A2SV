"""

https://codeforces.com/gym/523525/problem/B

PASSED

"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n
    dp [-1] = arr[-1]
    for i in reversed(range(n-1)):
        tot = arr[i]
        ind = i + arr[i]
        while ind < n:
            add = dp[ind]
            ind += add
            tot += add

        dp[i] = tot

    print(max(dp))