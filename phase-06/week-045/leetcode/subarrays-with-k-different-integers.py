class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # sliding window
        # to find the subs with k distinct elems, we could first find
        # the count of subs with at most k distinct nums, then find the count
        # of subs with at most k - 1 distinct nums, then we can subtract the 
        # latter from the former to remain with subs with EXACTLY k distinct elems

        return self.subsWithAtMostK(nums, k) - self.subsWithAtMostK(nums, k - 1)

    def subsWithAtMostK(self, nums, k):

        count = Counter()

        res = 0
        n = len(nums)
        l = 0
        for r in range(n):
            count[nums[r]] += 1

            while len(count) > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

            res += r - l + 1

        return res
        
