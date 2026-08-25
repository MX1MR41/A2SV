class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # dp
        # possible subsequences are all evens, all odds, interleaving 
        # so the answer would be the maximum of those three.
        # use dp to compute the interleaving option. if a number is odd,
        # we want to find the previously seen best even number's result.
        # Vice versa for even numbers 
        even = len([i for i in nums if not i % 2])
        odd = len([i for i in nums if i % 2])

        res = max(even, odd)

        last_odd = [-1, 0]
        last_even = [-1, 0]

        n = len(nums)
        dp = [1] * (n)

        for i in range(n):
            num = nums[i]
            if num % 2:
                if last_even[0] != -1:
                    dp[i] = last_even[1] + 1

                if dp[i] > last_odd[1]:
                    last_odd = [i, dp[i]]
            else:
                if last_odd[0] != -1:
                    dp[i] = last_odd[1] + 1

                if dp[i] > last_even[1]:
                    last_even = [i, dp[i]]

        res = max(res, max(dp))

        return res

        return res







        
