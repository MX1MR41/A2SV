class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) - k + 1 < 2 ** k:
            return False
        
        seen = [False] * (2**k)
        for i in range(len(s) - k + 1):
            b = ""
            for j in range(i, i + k):
                b += s[j]

            seen[int(b, 2)] = True


        return all(seen)
