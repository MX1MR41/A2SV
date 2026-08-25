class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # prefix technique
        # to find if a good sub exists in linear time, we can use prefix technique
        # where what is stored is the modulo of each cumulative sum by k
        # that way if we get a cumulative sum whose modulo by k is say X, and there
        # was another cumulaive sum with the same modulo result X, we can discard
        # the previous subarray and the remaining subarray is divisble by k.

        prefix = {0: -1} # initialize the index as right before the start of the array
        pre = 0
        
        for i in range(len(nums)):
            pre += nums[i]
            modulo = pre % k
            
            if modulo == 0 and i >= 1:
                return True

            # previously seen and of length greater than orequal to 2
            if modulo in prefix and prefix[modulo] <= i - 2:
                return True

            prefix[modulo] = min(prefix[modulo], i) if modulo in prefix else i

        return False
