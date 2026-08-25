class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # sorting + greedy
        # we want to space the numbers as wide apart as possible,
        # to do that we can modify every number to be the minimum possible unused value
        # we keep track of that minimum value and if it is possible to modify our current
        # number to turn it into that min number, we do so and we "occupy" that value
        # so the minimum unoccupied will now move one spot right

        nums.sort()
        min_free = nums[0] - k

        n = len(nums)
        for i in range(n):
            curr = nums[i]
            if curr - k > min_free:
                min_free = curr - k

            if curr - k <= min_free <= curr + k:
                nums[i] = min_free
                min_free += 1

        return len(set(nums))
