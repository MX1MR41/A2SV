# https://atcoder.jp/contests/dp/tasks/dp_d

N, W = list(map(int, input().split()))
items = []
for _ in range(N):
    items.append(list(map(int, input().split())))

dp = [[0] * (W + 1) for _ in range(N + 1)]

# an item can only be included once
for curr in range(1, N + 1):
    weight, value = items[curr - 1]
    for cap in range(W + 1):
        if cap < weight:  # the current capacity doesnt accomodate this weight
            dp[curr][cap] = dp[curr - 1][
                cap
            ]  # we do not include this item so we take the previous item's value
        else:
            # we can either not include the item and just take the last item's dp
            # or include the current item and recall the dp of the remaining weight's (cap - weight) dp
            dp[curr][cap] = max(dp[curr - 1][cap], dp[curr - 1][cap - weight] + value)

print(dp[-1][-1])
