class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res, n = float("inf"), len(blocks)
        # initializing a static sliding window
        l, r, wind = 0, k, blocks[:k]
        c = Counter(wind)
        w = c["W"] # count of W's in our initial window
        res = w

        while r < n:
            prev, nxt = blocks[l], blocks[r] 
            if prev == "W":
                w -= 1
            if nxt == "W":
                w += 1

            res = min(w, res)
            r += 1
            l += 1

        return res


        
        