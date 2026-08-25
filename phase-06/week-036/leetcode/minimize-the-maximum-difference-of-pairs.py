class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # binary search min-max, greedy
        if p == 0:
            return 0

        nums.sort()
        
        n = len(nums)
        

        def check(val):
            index, count = 0, 0
            while index < n - 1:
                
                if nums[index + 1] - nums[index] <= val:
                    count += 1
                    index += 1
                index += 1
            return count >= p
 
        left, right = 0, nums[-1] - nums[0]

        

        res = right
        while left <= right:
            mid = (left + right)//2
            
            if check(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
