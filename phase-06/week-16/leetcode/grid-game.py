class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # prefix sum + suffix sum
        # player 1 aims to minimize player 2's score, so at each index he will choose
        # to go down only if it will minimize player 2's score.
        # Precompute and store prefix and suffix sums for both arrays,
        # if player 1 decides to go down at i, his score will be up_prefix[i] + down_suffix[i],
        # consequently player 2's score will be max(down_prefix[i - 1], up_suffix[i + 1])
        # because all upper elements upto i will be zero and all down elements after i will be 0
        n = len(grid[0])

        up_prefix = grid[0][:]
        up_suffix = grid[0][:]
        down_suffix = grid[1][:]
        down_prefix = grid[1][:]

        for i in range(1, n):
            up_prefix[i] += up_prefix[i - 1]
            down_prefix[i] += down_prefix[i - 1]

        for i in range(n - 2, -1, -1):
            up_suffix[i] += up_suffix[i + 1]
            down_suffix[i] += down_suffix[i + 1]

        res = float("inf")
        for i in range(n):
            player_2 = 0
            if i > 0:
                player_2 = max(player_2, down_prefix[i - 1])

            if i < n - 1:
                player_2 = max(player_2, up_suffix[i + 1])

            res = min(res, player_2)

        return res

        
