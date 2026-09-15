class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        # dp
        # find all valid palindromes and group them by their end indices
        # then build up the result from bottom-up,
        # for every end index i, try all its palindromes and check the best answer
        # computed previouly for just before the start of each palindrome
        n = len(s)
        g = defaultdict(list)

        for i in range(n):
            start = i
            end = i + 1
            while start >= 0 and end < n and s[start] == s[end]:
                if end - start + 1 >= k:
                    g[end].append((start, end))
                start -= 1
                end += 1

            start = i
            end = i
            while start >= 0 and end < n and s[start] == s[end]:
                if end - start + 1 >= k:
                    g[end].append((start, end))

                start -= 1
                end += 1


        dp = [0 for _ in range(n)]
        for i in range(n):
            ps = g[i]
            curr = 0 if not ps else 1
            for s, e in ps:
                if s > 0:
                    curr = max(curr, dp[s - 1] + 1)

            dp[i] = curr
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])

        return dp[-1]
