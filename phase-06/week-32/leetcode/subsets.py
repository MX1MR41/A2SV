class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # bit manipulation
        # use a bitmask of length n( where n is len(nums)) and all bits set to 1
        # if n == 3, bitmask = 111, where 1 indicates that nums[i] should be included in the 
        # current subset that is represented by the current bitmask. Then, to go over all possible
        # subsets, we keep subtracting 1 from the bitmask until we eventually reach 0. 
        # 111 (7) -> 110 (6) -> 101 (5) -> 100 (4) -> 011 (3) -> 010 (2) -> 001 (1) -> 000 (0)
        # for every iteration of the bitmask, we build out subset based on whether an index's
        # bit is set to 1 or not

        n = len(nums)

        mask = (1 << n) - 1

        subsets = [[]]

        while mask:
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])

            subsets.append(subset)

            mask -= 1

        return subsets
        
