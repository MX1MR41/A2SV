class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        return heapq.nlargest(k,nums)[-1]
        
