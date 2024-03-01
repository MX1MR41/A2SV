class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # backtracking approach in which we try all possible combinations
        # of nums until 10 (exclusive) and if we find a valid answer, we store
        
        res = set()
        
        # params are the current number (1,2,3..9), the current combination
        # and the cumulative sum of the current combination
        def combine(num, comb, tot):
            #base cases
            if len(comb) > k or num > 10 or tot > n:
                return
            
            # a valid combo
            if tot == n and len(comb) == k:
                res.add(tuple(comb))
                return

            
            for i in range(num, 10):
                
                comb.append(i)
                tot += i
                # we recursively try combination with the next possible nums
                combine(i + 1, comb, tot)
                comb.pop()
                tot -= i

        combine(1, [], 0)

        return res
