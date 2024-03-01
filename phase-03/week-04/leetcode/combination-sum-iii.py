class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = set()
        
        def combine(num, comb, tot):
            print(comb, tot)
            if len(comb) > k or num > 10 or tot > n:
                return

            if tot == n and len(comb) == k:
                res.add(tuple(comb))
                return

            for i in range(num, 10):
                
                comb.append(i)
                tot += i
                combine(i + 1, comb, tot)
                comb.pop()
                tot -= i

        combine(1, [], 0)

        return res
