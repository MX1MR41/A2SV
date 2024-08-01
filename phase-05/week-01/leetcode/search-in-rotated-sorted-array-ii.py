class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:

                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1

            elif nums[mid] < nums[right]:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid

            else:
                right -= 1

        return nums[left] == target





# shorter version

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in nums:
            if i == target: return True

        return False
        
