class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))

        ops = 0

        while nums and nums[-1] > k:
            nums.pop()
            ops += 1


        if not nums:
            nums.append(k)

        return ops if len(nums) == 1 and nums[-1] == k else -1

        
