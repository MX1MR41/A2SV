class Solution:
    def answerString(self, word: str, numFriends: int) -> str: 
        # sliding window 

        splits = numFriends - 1

        n = len(word)

        window_size = n - splits

        res = ""

        l = 0
        for r in range(n):
            if r - l + 1 > window_size:
                l += 1
            curr = word[l: r + 1]
 
            res = max(res, curr)

        if splits != 0:
            while l <= r:
                curr = word[l: r+ 1]
                res = max(res, curr)
                l += 1

        return res
