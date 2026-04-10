class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float("inf")
        inds = defaultdict(list)

        for i, num in enumerate(nums):
            inds[num].append(i)

            if len(inds[num]) >= 3:

                arr = inds[num]

                curr = 2 * arr[-1] - 2 * arr[-3]

                res = min(res, curr)


        return res if res != float("inf") else -1


        
