class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if len(set([i for i in str(n)])) == 1 and "0" in str(n):
            return 0

        return sum([int(i) for i in str(n) if i != "0"]) * int("".join([i for i in str(n) if i != "0"]))
        
