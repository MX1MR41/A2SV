class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n))[2:][::-1]
        while len(s) < 32:
            s += "0"

        return int(s, 2)
        
