class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # sliding window
        
        count = Counter()
        res = 0
        n = len(s)

        l = 0
        for r in range(n):
            right = s[r]
            count[right] += 1

            while len(count) == 3:
                res += n - r
                left = s[l]
                count[left] -= 1
                if count[left] == 0:
                    del count[left]

                l += 1

        return res
        
