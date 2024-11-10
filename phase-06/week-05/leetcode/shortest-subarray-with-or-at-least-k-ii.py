class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # sliding window + bit manipulation
        # initialize an array that keeps count of each bit position's occurence
        # a window is valid if the cumulative OR of the non-zero bits in the frequency array is >= k

        def valid(arr):
            curr = 0
            for i in range(32):
                if arr[i]:
                    curr |= 1 << i

            return curr >= k



        ans = float("inf")
        curr = [0] * 32 # array to keep count of each bit

        l = 0
        for r in range(len(nums)):
            
            # add nums[r]'s bits into the frequency array
            num = nums[r]

            for i in range(32):
                if num & (1 << i):
                    curr[i] += 1

            while l <= r and valid(curr):
            
                ans = min(ans, r - l + 1)

                # deduct nums[l]'s bits from the frequency array
                num = nums[l]
                for i in range(32):
                    if num & (1 << i):
                        curr[i] -= 1
                #shrink window
                l += 1

        return ans if ans != float("inf") else -1
