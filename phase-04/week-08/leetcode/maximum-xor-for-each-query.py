class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # maximum XOR (i.e.) can be found by XOR-ing two numbers whose every bits are different
        # we need to find a k where k ^ current_array_xor = num of len maximumBit with all 1's
        # k ^ curr = 111 => k ^ 111 = curr
        tot = 0
        res = []
        mask = (2 ** (maximumBit)) - 1
        for i in nums:
            tot ^= i
            k = tot ^ mask
            res.append(k)

        return res[::-1]

        
        
