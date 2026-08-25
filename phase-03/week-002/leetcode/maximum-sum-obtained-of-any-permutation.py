class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)

        for start,end in requests:
            pre[start] += 1
            pre[end + 1] -= 1

        for i in range(1, n + 1):
            pre[i] += pre[i - 1]

        res = 0
        for a, b in zip(sorted(pre[:-1]), sorted(nums)):
            res += a * b
            
        return res % (10**9 + 7)
