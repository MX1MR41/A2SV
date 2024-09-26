# https://atcoder.jp/contests/dp/tasks/dp_o

MOD = 10**9 + 7

def count_pairings(N, compatibility):
    dp = [0] * (1 << N)
    dp[0] = 1  # Base case: one way to pair no men and no women

    for mask in range(1 << N):
        # Count how many men are already paired in this mask
        man_index = bin(mask).count('1')
        
        if man_index >= N:
            continue
        
        for woman_index in range(N):
            # Check if woman_index is not yet paired and is compatible with current man_index
            if compatibility[man_index][woman_index] == 1 and not (mask & (1 << woman_index)):
                # Update the dp table for the new mask
                new_mask = mask | (1 << woman_index)
                dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD

    return dp[(1 << N) - 1]


N = int(input())
mat = []
for _ in range(N):
  row = list(map(int, input().split()))
  mat.append(row)

print(count_pairings(N, mat)) 
