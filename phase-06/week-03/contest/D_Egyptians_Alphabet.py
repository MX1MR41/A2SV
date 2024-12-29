MOD = 10**9 + 7

def mod_exp(a, b, mod):
    result = 1
    while b:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result


import sys
input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
a = list(map(int, data[2:n + 2]))
b = list(map(int, data[n + 2:2 * n + 2]))

p = 1  # Probability of previous positions being equal
ans = 0

for i in range(n):
    if a[i] != 0 and b[i] != 0:
        if a[i] > b[i]:
            ans = (ans + p) % MOD
            break
        elif a[i] < b[i]:
            break
    elif a[i] == 0 and b[i] != 0:
        ans = (ans + p * (m - b[i]) % MOD * mod_exp(m, MOD - 2, MOD)) % MOD
        p = (p * mod_exp(m, MOD - 2, MOD)) % MOD
    elif a[i] != 0 and b[i] == 0:
        ans = (ans + p * (a[i] - 1) % MOD * mod_exp(m, MOD - 2, MOD)) % MOD
        p = (p * mod_exp(m, MOD - 2, MOD)) % MOD
    elif a[i] == 0 and b[i] == 0:
        ans = (ans + p * (m - 1) % MOD * mod_exp(2 * m, MOD - 2, MOD)) % MOD
        p = (p * mod_exp(m, MOD - 2, MOD)) % MOD

print(ans % MOD)

