class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        for i in range(len(nums)):
            curr = nums[i]
            ans.append(curr)
            for j in range(i+1, len(nums)):
                curr += nums[j]
                ans.append(curr)

        
        ans.sort()

        return sum(ans[left - 1: right]) % (10**9 + 7)

                
        
