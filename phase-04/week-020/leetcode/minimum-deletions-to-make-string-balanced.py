class Solution:
    def minimumDeletions(self, s: str) -> int:
        # find a dividing point where the answer could be minimized
        n = len(s)
        a = s.count("a")
        b = 0

        ans = n

        for ch in s:
            if ch == "a":
                a -= 1

            ans = min(ans, a + b)

            if ch == "b":
                b += 1

        return ans


        
