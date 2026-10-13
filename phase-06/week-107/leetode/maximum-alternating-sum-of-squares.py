class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: abs(x), reverse = True)
        arr = []
        n = len(nums)
        i, j = 0, len(nums) - 1
        while i <= j:
            arr.append(nums[i])
            if j > i:
                arr.append(nums[j])

            i += 1
            j -= 1

        sign = 1
        tot = 0
        for i in range(n):
            tot += sign * arr[i]**2
            sign = 0 - sign

        return tot
        
