class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        res = nums[l]

        while l <= r:
            lnum, rnum = nums[l], nums[r]
            # if the portion of the array nums[l:r+1] is already sorted
            if lnum < rnum:
                res = min(res, lnum)
                break

            mid = (l+r)//2
            mnum = nums[mid]
            res = min(res, mnum)
            # if the mid happens to be greater than the l num, 
            # that means nums[l:mid+1] is already sorted, so we search to the right
            # else it means that means the pivot where the largest and smallest meet
            # is to the left of mid so we search left
            if mnum >= lnum:
                l = mid + 1
            
            else:
                r = mid - 1


        return res
        