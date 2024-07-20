MAX = 10 ** 5 + 1
MOD = 10 ** 9 + 7
t, k = map(int, input().split())

prefix = [1] * MAX
prefix[0] = 0

prefix[k] = 2

for i in range(k + 1, MAX):
    prefix[i] = (prefix[i - 1] + prefix[i - k]) % MOD 

for i in range(1, MAX):
    prefix[i] = (prefix[i] + prefix[i - 1]) % MOD

for _ in range(t):
    a, b = map(int, input().split())
    print((prefix[b] - prefix[a - 1]) % (10 ** 9 + 7))