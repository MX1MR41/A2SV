class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pre = []
        p = 0
        for i in nums:
            if i == target:
                p += 1

            pre.append(p)

        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i, n):

                cnt = pre[j] - pre[i - 1] if i - 1 >= 0 else pre[j]

                if cnt > (j - i + 1)//2:
                    res += 1

        return res
        
