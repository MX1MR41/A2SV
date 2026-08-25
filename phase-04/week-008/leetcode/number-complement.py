class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << num.bit_length()) # shift 1 to front of the highest bit
        mask -= 1 # to make all bits 1 i.e. 1000 - 1 = 0111
        return num ^ mask # 0^1 = 0, 1^1 = 0, 101(5) ^ 111 = 010
