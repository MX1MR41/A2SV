# https://atcoder.jp/contests/dp/tasks/dp_k

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

dp = [False] * (K + 1) # dp[i] = True if the player whose turn it is can win with i stones remaining

for stones in range(1, K + 1):
    for choice in A:
        if stones >= choice and not dp[stones - choice]: #dp[stones - choice] = False if the opponent can't win with dp[i-a] stone left
            dp[stones] = True # the current player can win
            break
if dp[K]:
  print("First")
else:
  print("Second")

