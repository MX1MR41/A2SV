class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # binary search
        nonzero = any([i > 0 for i in nums])
        if not nonzero:
            return 0

        def check(k):
            pre = [0] *(len(nums))
            for l, r, v in queries[:k + 1]:
                pre[l] += v
                if r + 1 < len(pre):
                    pre[r + 1] -= v

            for i in range(1, len(pre)):
                pre[i] += pre[i - 1]

            zero = True
            for i in range(len(nums)):
                curr = nums[i] - pre[i]
                if curr > 0:
                    zero = False

                    break

            return zero


        l, r = 0, len(queries) - 1
        res = -1
        while l <= r:
            mid = (l + r)//2
            if check(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res + 1 if res != -1 else -1
        
