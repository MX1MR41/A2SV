class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # sliding window + bit manipulation
        # keep expanding right until you have a valid window, 
        # then while the window is valid, keep shrinking from the left

        n = len(nums)

        max_or_arr = []
        max_or = 0
        for i in range(n - 1, -1, -1):
            num = nums[i]
            max_or |= num
            max_or_arr.append(max_or)

        max_or_arr.reverse()

        def valid(l, wind):
            max_or = max_or_arr[l]

            for i in range(30):
                if (max_or & (1 << i)) and not wind[i]:
                    return False

            return True


        res = []
        wind = [0] * 30

        l = 0
        for r in range(n):
            num = nums[r]

            for j in range(30):
                if num & (1 << j):
                    wind[j] += 1

            while l <= r and valid(l, wind):
                lenn = r - l + 1
                res.append(lenn)
                for j in range(30):
                    if nums[l] & (1 << j):
                        wind[j] -= 1

                l += 1

        return res
