class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for num in nums:
            tot = sum([int(i) for i in str(num)])
            d[tot].append(num)

        res = 0
        for s in d:
            vals = d[s]
            vals.sort()
            if len(vals) > 1:
                res = max(res, sum(vals[-2:]))


        return res if res else -1
        
