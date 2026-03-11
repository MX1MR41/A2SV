class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
            
        bit_len = n.bit_length()
        
        mask = (1 << bit_len) - 1
        
       
        return n ^ mask
