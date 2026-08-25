class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # modified binary search
        # at each iteration, we check which portion of the array is sorted
        # and base our decision based on that
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == target:
                return l

            if nums[r] == target:
                return r

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # if left portion is sorted and target is in between, we search there
            if nums[l] <= nums[mid]:  
                if nums[l] <= target <= nums[mid]:  
                    r = mid - 1
                else:  
                    l = mid + 1

            # if right portion is sorted and target is in between, we search there        
            else:  
                if nums[mid] <= target <= nums[r]:  
                    l = mid + 1
                else:  
                    r = mid - 1

        return -1
