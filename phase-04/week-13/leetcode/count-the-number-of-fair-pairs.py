class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # sorting + binary search
        # for each num, find the the first next num which would make their sum >= lower
        # and find last next num which would make their sum <= upper
        # the number of elements in between (hi - lo + 1) are all the valid choices
        n = len(nums)
        count = 0
        nums.sort()


        for i in range(n - 1):
            l, r = i + 1, n - 1
            hi, lo = l, r

            while l <= r:
                mid = (l + r)//2
                if nums[mid] + nums[i] >= lower:
                    lo = mid
                    r = mid - 1
                else:
                    l = mid + 1

            l, r = i + 1, n - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] + nums[i] <= upper:
                    hi = mid
                    l = mid + 1
                else:
                    r = mid - 1


            if lower <= nums[i] + nums[lo] and nums[i] + nums[hi] <= upper:
                count += hi - lo + 1

        return count
            
            


        
