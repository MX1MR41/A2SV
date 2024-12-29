"""

PASSED

"""

MOD = 10**9 + 7
k = int(input())
nodes = pow(2, k) - 2
tot = pow(4, nodes, MOD)
tot = (tot * 6) % MOD

print(tot)
