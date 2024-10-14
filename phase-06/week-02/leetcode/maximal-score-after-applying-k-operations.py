class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)
        ans = 0
        for _ in range(k):
            curr = -heappop(nums)
            ans += curr
            heappush(nums, -ceil(curr/3))

        return ans
        
