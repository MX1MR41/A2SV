class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = defaultdict(lambda : float("-inf"))

        res = float("inf")
        for i in range(len(nums)):
            curr = str(nums[i])

            res = min(res, i - seen[curr])

            rev = str(curr)[::-1].lstrip('0')
            
            seen[rev] = i


        seen = defaultdict(lambda : float("inf"))
        # res = float("inf")
        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            rev = str(curr)[::-1].lstrip('0')

            res = min(res, seen[rev] - i)

            
            seen[str(curr)] = i




        return res if res != float("inf") else -1

        
