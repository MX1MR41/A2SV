class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # we use a binary search approach to search over the possible outputs
        # ranging from the max of the array to the sum of the array
        # the reason the range starts from max of the array is because
        # splitting the array into single elements would give us that answer
        # and the sum is the upper limit because the whole array bounds all sums
        l, r = max(nums), sum(nums)
        n = len(nums)

        # initialize it to the worst result we can get
        res = r

        while l <= r:
            mid = (l+r)//2

            # counts valid number of segments we can get by segmenting
            # into subarrays whose sum is less than or equal to mid
            segments = 1
            
            curr_sum = 0
            for i in range(n):
                if curr_sum + nums[i] > mid:
                    segments += 1
                    curr_sum = 0

                curr_sum += nums[i]

            # meaning that the current value of mid is too small
            # and causes too many segments
            if segments > k:
                l = mid + 1
            # meaning it is a valid segmentation valuue of mid, we shrink further
            # to the left to even find a smaller possible value
            else: 
                res = min(res, mid)
                r = mid - 1

        return res

        