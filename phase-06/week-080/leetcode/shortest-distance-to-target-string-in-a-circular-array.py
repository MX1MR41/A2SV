class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1

        res = float("inf")

        i = startIndex
        steps = 0
        while words[i] != target:
            i = (i + 1) % len(words)
            steps += 1

        res = min(res, steps)

        i = startIndex
        steps = 0
        while words[i] != target:
            i = (i - 1) % len(words)
            steps += 1

        res = min(res, steps)

        return res
        
