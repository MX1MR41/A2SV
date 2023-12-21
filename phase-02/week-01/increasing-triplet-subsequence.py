class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        MIN = max(nums)
        MAX = MIN
        ans = False

        for i in nums:

            if i <= MIN:
                MIN = i

            elif i <= MAX:  
                MAX = i
                
            else: # the number is in between MIN and MAX
                ans = True
                break

        return ans