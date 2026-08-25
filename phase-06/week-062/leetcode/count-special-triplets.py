class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 1000000007

        res = 0
        right = Counter(nums)
        left = Counter()

        n = len(nums)

        for i in range(n):
            num = nums[i]
            right[num] -= 1

            res = (res + left[2 * num] * right[2 * num]) % MOD

            left[num] += 1

        return res
        
