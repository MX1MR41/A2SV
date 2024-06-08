"""

https://codeforces.com/gym/522079/problem/F

"""

from sys import stdin


def input(): return stdin.readline().strip()

T = int(input())

for _ in range(T):
    N = int(input())
    x = list(map(int, input().split()))

    MOD = 1000_000_007
    bit_counts = [0]*60
    for xi in x:
        for i in range(60):
            if xi&(1<<i):
                bit_counts[i] += 1
    ans = 0
    for xi in x:
        tot_or = tot_and = 0
        for i in range(60):
            if xi&(1<<i):
                tot_or += (1<<i)%MOD*N
                tot_or %= MOD
                tot_and += (1<<i)%MOD*bit_counts[i]
                tot_and %= MOD
            else:
                tot_or += (1<<i)%MOD*bit_counts[i]
                tot_or %= MOD
        ans += tot_or*tot_and
        ans %= MOD

    print(ans)