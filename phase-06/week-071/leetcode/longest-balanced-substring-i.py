class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 1

        n = len(s)

        for l in range(n):
            cnt = Counter()
            freq = Counter()

            for r in range(l, n):
                rlet = s[r]
                pf = cnt[rlet]
                nf = pf + 1
                cnt[rlet] = nf

                freq[nf] += 1

                if pf > 0:
                    freq[pf] -= 1
                    if freq[pf] == 0:
                        del freq[pf]

                
                if len(freq) == 1:
                    res = max(res, r - l + 1)

        return res
        
