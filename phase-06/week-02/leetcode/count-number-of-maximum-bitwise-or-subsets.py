class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        _max = 0
        for i in nums:
            _max |= i

        def dfs(ind, totor, seen):
            nonlocal total
            if ind == n:
                return
            if totor == _max:
                total += 1

            for i in range(ind + 1, n):
                dfs(i, totor | nums[i], seen + str(nums[i]))

        dfs(-1, 0, "")
        return total
