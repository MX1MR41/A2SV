class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # modified code from max consecutive-ones-iii
        # https://leetcode.com/problems/max-consecutive-ones-iii/
        n = len(answerKey)
        l, F, T, res = 0, 0, 0, 0
        # find the max length for consecutive T's first
        for r in range(n):
            if answerKey[r] == "F":
                F += 1
            while F > k:
                if answerKey[l] == "F":
                    F -= 1
                l += 1
            res = max(res, r-l + 1)

        # then find the max length for consecutive F's 
        l = 0
        for r in range(n):
            if answerKey[r] == "T":
                T += 1
            while T > k:
                if answerKey[l] == "T":
                    T -= 1
                l += 1
            res = max(res, r-l + 1)

        return res
        