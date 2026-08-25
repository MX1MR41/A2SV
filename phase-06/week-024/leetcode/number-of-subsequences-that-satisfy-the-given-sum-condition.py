class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # binary search + two pointers
        # find the right boundary, then compute the number of possible subsequences
        # using the formula 2**n - 1, because subs(1) = 1, subs(2) = 3, subs(3) = 7 ...
        # we can generalize a formula 2**n - 1 subs can be generated from n elements
        MOD = 10**9 + 7
        nums.sort()
        res = 0
        n = len(nums)


        def search(l, r, x):
            res = l
            while l <= r:
                mid = (l + r)//2
                if nums[mid] <= x:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1

            return res



        for i in range(n):

            r = search(i, len(nums) - 1, target - nums[i])

            if nums[i] + nums[r] <= target:
                m = r - i
                res += (max(0, 2**m - 1 ) + 1) % MOD


        return res % MOD




