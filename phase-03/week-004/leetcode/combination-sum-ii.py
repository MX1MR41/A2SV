class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # modified code from Combination Sum problem
        # https://leetcode.com/problems/combination-sum/
        res = set()
        candidates.sort()

        def dfs(curr, tot, start):

            if tot > target:
                return

            if tot == target:
                res.add(tuple(curr))
                return

            for i in range(start, len(candidates)):

                # if the number is duplicatet, we need to skip it
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                curr.append(candidates[i])
                dfs(curr, tot + candidates[i], i+1)  
                curr.pop()

        dfs([], 0, 0)

        return res