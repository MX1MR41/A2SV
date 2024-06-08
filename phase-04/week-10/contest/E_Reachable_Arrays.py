"""

https://codeforces.com/gym/524965/problem/E

"""

MOD = 998244353

def solve():
    
    n = int(input())
    a = list(map(int, input().split()))

    
    next_min = [0] * n
    dp_sum = [0] * (n + 2)
    dp_next = [0] * n

    stack_min = []
    next_min[n - 1] = n
    dp_sum[n] = 1

    
    for pos in range(n - 1, -1, -1):
        while stack_min and a[stack_min[-1]] > a[pos]:
            stack_min.pop()
        next_min[pos] = n if not stack_min else stack_min[-1]
        stack_min.append(pos)

        nxt_pos = next_min[pos]
        dp_pos = (dp_sum[pos + 1] - dp_sum[nxt_pos + 1]) % MOD
        if nxt_pos != n:
            dp_pos = (dp_pos + dp_next[nxt_pos]) % MOD
            dp_next[pos] = (dp_sum[nxt_pos] - dp_sum[nxt_pos + 1] + dp_next[nxt_pos]) % MOD

        dp_sum[pos] = (dp_pos + dp_sum[pos + 1]) % MOD

    
    res = 0
    mn = a[0]
    for i in range(n):
        mn = min(mn, a[i])
        if a[i] == mn:
            res = (res + dp_sum[i] - dp_sum[i + 1]) % MOD
    print(res)


t = int(input())
for _ in range(t):
    solve()
