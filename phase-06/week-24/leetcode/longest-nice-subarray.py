class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # bit manipulation + sliding window
        def invalid(d):
            for i in d:
                if d[i] > 1:
                    return True

            return False



        l = 0
        res = 0
        d = Counter()
        for r in range(len(nums)):
            num = nums[r]
            for b in range(32):
                if num & (1 << b):
                    d[b] += 1

            while invalid(d):
                lnum = nums[l]
                for b in range(32):
                    if lnum & (1 << b):
                        d[b] -= 1

                l += 1

            res = max(res, r - l + 1)


        return res

                    
        
