class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        n = len(nums)
        res = []
        for i in range(n - 1):
            a = nums[i]
            if a in seen: # to prevent duplicates
                continue
            seen.add(a)
            l = i + 1
            r = n - 1
            while l < r:
                b, c = nums[l], nums[r]
                tsum = a + b + c

                if tsum == 0:
                    res.append([a,b,c])
                    while l < r and nums[l] == b:
                        l += 1
                    while r > l and nums[r] == c:
                        r -= 1
                elif tsum < 0:
                    while l < r and nums[l] == b:
                        l += 1
                elif tsum > 0:
                    while r > l and nums[r] == c:
                        r -= 1
                
        return res