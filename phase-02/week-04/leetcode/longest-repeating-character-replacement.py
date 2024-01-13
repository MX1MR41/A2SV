class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # modified code from maximize-the-confusion-of-an-exam
        # https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
        chrs = list(set(s))
        n, c = len(s), len(chrs)
        # if there is only one character, we wont need to make any changes
        if c == 1:
            return n

        res = 0
        for _ in range(c): # we iterate through the list of letters without repeatition
            chr = chrs.pop() # the current letter whose max length we shall be checking for
            l, cnt = 0, 0

            for r in range(n):
                if s[r] != chr:
                    cnt += 1

                # shrinking the window from the left
                while l < r and cnt > k:
                    if s[l] != chr:
                        cnt -= 1
                    l += 1

                res = max(res, r-l + 1)



        return res
        