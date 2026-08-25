class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # when we remove an element we need to know the sum of the remaining elements
        # create a prefix sum to store the sum of even and odd indices before that number
        # create a suffix sum to store the sum of even and odd indices after that number
        # if odds and evens summation in the prefix and suffix of an index match,
        # then we can remove that number safely
        pref = []
        p = (0, 0)
        odd = True
        for i in nums:
            currp = (p[0] + i, p[1]) if odd else (p[0], p[1] + i)
            pref.append(currp[::])
            p = currp
            odd = not odd

        odd = True if len(nums) % 2 else False

        suff = []
        s = (0, 0)
        for i in nums[::-1]:
            currs = (s[0] + i, s[1]) if odd else (s[0], s[1] + i)
            suff.append(currs[::])
            s = currs
            odd = not odd

        suff.reverse()

        ans = 0

        for i in range(len(nums)):
            s, p = suff[i], pref[i]
            if s[0] + p[1] == s[1] + p[0]:
                ans += 1

        return ans
