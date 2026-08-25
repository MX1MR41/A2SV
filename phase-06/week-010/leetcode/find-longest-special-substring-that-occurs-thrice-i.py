class Solution:
    def maximumLength(self, s: str) -> int:
        ans = -1
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                count = 0

                size = j - i

                for k in range(size, n + 1):

                    if s[k - size : k] == sub:
                        count += 1

                if count >= 3 and len(set(sub)) == 1:
                    
                    ans = max(ans, size)

        return ans
