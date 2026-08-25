class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # backtracking + dp
        # keep track of the turn; if it's alice's turn, we maximize her score
        # else we minimize her score
        n = len(piles)

        dp = {}

        def alice(turn, ind, M):
            if ind == n: return 0

            if (turn, ind, M) in dp: return dp[(turn, ind, M)]

            res = 0 if turn else float("inf")

            curr = 0

            for X in range(1, 2*M + 1):
                if ind + X > n: break

                curr += piles[ind + X - 1]

                if turn:
                    res = max(res, curr + alice(not turn, ind + X, max(X, M)))
                else:
                    res = min(res, alice(not turn, ind + X, max(M, X)))

            dp[(turn, ind, M)] = res
            return res

        return alice(True, 0, 1)
