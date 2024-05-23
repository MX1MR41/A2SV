# https://atcoder.jp/contests/dp/tasks/dp_e
N, W = map(int, input().split())
items = []

for _ in range(N):
    items.append(tuple(map(int, input().split())))


tot = sum(item[1] for item in items)

dp = [[float("inf")] * (tot + 1) for _ in range(N + 1)]
dp[0][0] = 0

for curr in range(1, N + 1):
    weight, value = items[curr - 1]
    for cap in range(tot + 1):
        dp[curr][cap] = dp[curr - 1][cap]
        if cap >= value:
            dp[curr][cap] = min(dp[curr][cap], dp[curr - 1][cap - value] + weight)

res = 0
for cap in range(tot + 1):
    if dp[N][cap] <= W:
        res = cap

print(res)
