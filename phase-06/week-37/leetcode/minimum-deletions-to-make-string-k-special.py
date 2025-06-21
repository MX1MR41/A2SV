class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # greedy
        cnt = Counter(word)
        freqs = list(cnt.values())
        freqs.sort()
        

        res = float("inf")
        
        n = len(freqs)
        for i in range(n):
            dels = 0
            
            for j in range(i):
                dels += freqs[j]

            for j in range(i + 1, n):
                dels += max(0, (freqs[j] - (freqs[i] + k)))


            res = min(res, dels)

        return res

