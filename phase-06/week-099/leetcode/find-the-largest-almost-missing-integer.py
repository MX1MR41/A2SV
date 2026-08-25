class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        res = -1
        
        kcnt = defaultdict(lambda : set())

        n = len(nums)

        if k > n:
            return res

        for i in range(n):
            l = min(k - 1, i)
            r = min(k - 1, n - i - 1)

            if l + r + 1 < k:
                continue

            for j in range(i - l, i + 1):
                if (j + k - 1 > i + r):
                    break
                kcnt[nums[i]].add((j, j + k - 1))

        for x, subs in kcnt.items():
            if len(subs) == 1:
                res = max(res, x)

        return res

            

        
