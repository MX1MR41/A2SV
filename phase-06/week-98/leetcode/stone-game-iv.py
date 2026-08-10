class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp
        # the brute force solution would be to start from n and try deducting one of the possible 
        # square numbers, and then keep doing that for every path and see if at any point 
        # n can become zero while it is bob's turn, so basically backracking
        # but it can be optimized using dynamic programming
        # instead of starting from n and go to zero, start from 0 and build up to n
        # there are around 300 square numbers upto 10^5, which means for any number i, you can check
        # what deducting a given square number would take you to, for all square numbers.
        # At a given value i, if it is Alice's turn now, she can win if there is any prev_i 
        # (where prev_i = i - square_number) such that if it was Bob's turn, Bob would lose
        # or Alice would win

        # gather all the square numbers
        s = []
        i = 1
        while i ** 2 <= 100000:
            s.append(i ** 2)
            i += 1

        # dp[i] = [who can win if it is Alice's turn, who can win if it is Bob's turn]
        dp = [["", ""] for _ in range(n + 1)]

        # if 0 stones are left and it is Alice's turn, Bob wins. If it is Bob's turn, Alice wins
        dp[0] = ["B", "A"]

        # if 1 stone is left and it is Alice's turn, Alice wins. If it is Bob's turn, Bob wins
        dp[1] = ["A", "B"]

        for i in range(2, n + 1):
            # params for when it is Alice's turn
            canAliceWin = canAliceLose = False

            # params for when it is Bob's turn
            canBobWin = canBobLose = False
            for j in s:
                if j > i:
                    break

                prev = i - j

                # an unreachable state, skip
                if dp[prev] == ["", ""]:
                    continue

                if dp[prev][1] == "A":
                    canAliceWin = True

                if dp[prev][1] == "B":
                    canAliceLose = True

                if dp[prev][0] == "A":
                    canBobLose = True

                if dp[prev][0] == "B":
                    canBobWin = True



            if canAliceWin:
                dp[i][0] = "A"
            elif canAliceLose:
                dp[i][0] = "B"

            if canBobWin:
                dp[i][1] = "B"
            elif canBobLose:
                dp[i][1] = "A"


        return dp[-1][0] == "A"





                

        
