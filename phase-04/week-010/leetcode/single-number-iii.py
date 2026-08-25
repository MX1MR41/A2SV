class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # after xor-ing all elements we'll be left with the xor of the two unique elements
        # since the xor is a representation of the bit positions with different values for 
        # the two nums, wherever the two nums are different at a bit position, the bit of xor
        # will be 1. If we find the rightmost set bit of the xor(first bit where they differ)
        # and AND them with a mask wwith where only that bit is set as 1, we are guaranteed
        # that one of them will give a result 0 (because that num's bit position is 0) 
        # wile the other will give a result different from (cuz it's bit there is set as 1)
        tot = 0
        for i in nums:
            tot ^= i

        mask = tot & -tot


        x = y = 0
        for num in nums:
            if num & mask:
                x ^= num
            else:
                y ^= num

        return [x,y]
        
