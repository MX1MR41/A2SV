class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []

        for i in range(0, len(s), k):
            group = ""
            for j in range(i, i + k):
                if j >= len(s):
                    group += fill
                else:
                    group += s[j]

            res.append(group)


        return res
        
