class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        intervals = []

        n = len(nums)

        for i in range(n):
            if nums[i] == key:
                interval = [max(0, i - k), min(i + k, n - 1)]
                if intervals:
                    if interval[0] <= intervals[-1][1]:
                        intervals[-1][1] = max(intervals[-1][1], interval[1])
                    else:
                        intervals.append(interval)

                else:
                    intervals.append(interval)


        res = []
        for l, r in intervals:
            for i in range(l, r + 1):
                res.append(i)

        return res
        
