class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # prefix sum + bit manipulation
        # for every prefix XOR starting from the last, the number that would maximize
        # would be a number which has oppositely set bits than that prefix

        pre = 0

        ans = []

        for i in nums:
            pre ^= i
            num = 0
            for i in range(maximumBit):
                mask = 1 << i 
                # if the ith bit in pre is 0, make it 1 in num
                if pre & mask == 0:
                    num |= mask

            ans.append(num)
            
        ans.reverse()


        return ans
