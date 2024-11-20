class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # sliding window
        # since all the elements we will be taking are from the ends of the array,
        # there will always be a remaining subarray in the middle
        # so we find a subarray whom if chosen the remaining ends of the array contain
        # k of each letter

        
        n = len(s)

        # invalid case, there aren't enough elements to begin with
        if 3*k > n:
            return -1

        tota, totb, totc = s.count("a"), s.count("b"), s.count("c")

        res = float("inf")

        l = 0
        a = b = c = 0
        for r in range(n):
            curr = s[r]
            if curr == "a": a += 1
            if curr == "b": b += 1
            if curr == "c": c += 1

            rema, remb, remc = tota - a, totb - b, totc - c
            
            # shrink the window from the left as long as the remaining ends don't contain
            # k of each element
            while l < r and (rema < k or remb < k or remc < k):
                left = s[l]
                if left == "a":
                    rema += 1
                    a -= 1
                if left == "b":
                    remb += 1
                    b -= 1
                if left == "c":
                    remc += 1
                    c -= 1

                l += 1

            if rema >= k and remb >= k and remc >= k:
                res = min(res, l + n - r - 1)

        if res == float("inf"):
            if tota < k or totb < k or totc < k:
                return -1
                
            return n

        return res

