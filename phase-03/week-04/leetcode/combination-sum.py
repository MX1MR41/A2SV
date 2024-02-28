class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        res = set()
        candidates.sort() # sorting helps to eliminate target-exceeding combinations earlier

        def dfs(curr, tot, start):
            if tot > target:
                return 
            
            if tot == target:
                res.add(tuple(curr[:]))
                return

            # iterating from the "start" index instead of the actual start of the array
            # helps by pruning duplicate combinations
            for i in range(start, len(candidates)):

                if tot + candidates[i] > target:
                    break

                curr.append(candidates[i])
                dfs(curr, tot + candidates[i], i)  
                curr.pop()

        dfs([], 0, 0)

        return res
