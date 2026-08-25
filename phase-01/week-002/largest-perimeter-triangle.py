class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0 

        l, r = 0 , 2 # left pointer

        while r < len(nums): # right pointer

            a, b , c = nums[l], nums[l+1] , nums[r] 
            curr = a + b + c # current sum

            if a + b > c and a + c > b and b + c > a:
                if curr > sum:
                    sum = curr
            
            r += 1
            l += 1

        return sum

        