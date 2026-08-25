class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        n = len(nums)
        nums += nums
        dp = [float("inf") for _ in range(n)]

        left = defaultdict(lambda : float("-inf"))

        for i in range(2*n):
            dp[(i) % n] = min(dp[(i) % n], i - left[nums[i]])

            left[nums[i]] = i

        
        right = defaultdict(lambda : float("inf"))

        for i in range(2*n - 1, -1, -1):
            dp[(i)%n] = min(dp[(i)%n], right[nums[i]] - i)

            right[nums[i]] = i

        res = []
        for q in queries:
            if dp[q] == float("inf") or dp[q] == n:
                res.append(-1)
            else:
                res.append(dp[q])

        return res
            
        
