class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if i == j:
                    continue

                if nums[i] == nums[j]:
                    if not (i*j)%k:
                        cnt += 1

        return cnt