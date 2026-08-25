class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0

        for i in range(n):

            GCD = 0

            for num in nums[i:]:
                GCD = gcd(GCD, num)
                if GCD == k:
                    res += 1
                    
        return res
        