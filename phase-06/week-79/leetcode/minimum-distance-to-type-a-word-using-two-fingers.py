class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)

        def get_dist(finger_pos, target_pos):
            if finger_pos == 26:
                return 0
            r1, c1 = finger_pos // 6, finger_pos % 6
            r2, c2 = target_pos // 6, target_pos % 6
            return abs(r1 - r2) + abs(c1 - c2)

        dp = [
            [[float("inf") for _ in range(27)] for _ in range(27)] for _ in range(n + 1)
        ]

        dp[0][26][26] = 0

        for i in range(n):
            target = ord(word[i]) - ord("A")

            for f1 in range(27):
                for f2 in range(27):

                    if dp[i][f1][f2] == float("inf"):
                        continue

                    current_cost = dp[i][f1][f2]

                    cost1 = current_cost + get_dist(f1, target)
                    dp[i + 1][target][f2] = min(dp[i + 1][target][f2], cost1)

                    cost2 = current_cost + get_dist(f2, target)
                    dp[i + 1][f1][target] = min(dp[i + 1][f1][target], cost2)

        ans = float("inf")
        for f1 in range(27):
            for f2 in range(27):
                ans = min(ans, dp[n][f1][f2])

        return ans
