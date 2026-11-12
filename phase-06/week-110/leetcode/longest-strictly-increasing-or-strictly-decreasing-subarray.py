class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        up = True
        res = 1
        curr = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if up:
                    up = False
                    curr = 2

                else:
                    curr += 1
            
            elif nums[i] > nums[i - 1]:
                if up:
                    curr += 1
                else:
                    up = True
                    curr = 2
                
            else:
                curr = 1
                up = True


            res = max(res, curr)


        return res
        
