class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # binary search

        def check(x):
            count = 0
            last = -2
            for i in range(len(nums)):
                
                if nums[i] <= x:
                    
                    if last != i - 1:
                        
                        count += 1
                        last = i

            return count >= k


        l, r = min(nums), max(nums)
        res = r

        while l <= r:
            mid = (l + r)//2
            if check(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
    
