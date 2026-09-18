class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first, last = {}, {}
        for i, c in enumerate(s):
            first.setdefault(c, i)
            last[c] = i

        candidates = []
        for c, i in first.items():
            end = last[c]
            j = i
            valid = True
            while j <= end:
                ch = s[j]
                if first[ch] < i:     
                    valid = False
                    break
                end = max(end, last[ch])
                j += 1
            if valid:
                candidates.append((i, end))

        candidates.sort(key=lambda x: (x[1], x[0])) 

        res, prev_end = [], -1
        for st, en in candidates:
            if st > prev_end:
                res.append(s[st:en + 1])
                prev_end = en
        return res
