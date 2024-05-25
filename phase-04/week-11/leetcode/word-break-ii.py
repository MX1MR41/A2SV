class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[] for _ in range(n)]
        words = set(wordDict)

        if s[-1] in words:
            dp[-1].append(s[-1])

        for i in reversed(range(n)):
            for j in range(i, n):
                curr = s[i:j+1]
                if curr in words:
                    if j == n - 1:
                        dp[i].append(curr)
                    else:
                        nxt = dp[j + 1]
                        if nxt:
                            for word in nxt:
                                dp[i].append(curr + "," + word)

        res = []
        for group in dp[0]:
            res.append(" ".join(group.split(",")))

        return list(set(res))
