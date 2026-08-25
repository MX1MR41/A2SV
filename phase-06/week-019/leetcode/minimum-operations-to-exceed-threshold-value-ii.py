class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ops = 0
        while nums and len(nums) >= 2 and nums[0] < k:
            a = heappop(nums)
            b = heappop(nums)

            x = min(a, b)*2 + max(a, b)
            heappush(nums, x)
            ops += 1

        return ops

        
