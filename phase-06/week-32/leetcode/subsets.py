class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # bit manipulation
        # we initlaize a bitmask with bits set for every num in nums
        # i.e. if nums = [2, 3, 5] the bitmask will have the 2th, 3th and 5th bit set
        # bitmask |= (1 << 2), bitmask |= (1 << 3), bitmask |= (1 << 5), bitmask = 101100
        # then to find all the subsets, we can keep subtracting 1 from our bitmask, and this 
        # will force the bitmask to iterate over every possible combination of bits 
        # from bitmask (101100) upto 000000. And to ensure we don't process a combination with
        # foreign nums (nums that we didn't originally have) like 000111, we AND it with our
        # original bitmask so that only the original nums remain, 000111 & 101100 = 000100.

        mask = 0

        for i in nums:
            i += 10
            mask |= 1 << i

        init = mask

        res = []
        while mask:
            curr = []
            for i in range(32):
                if mask & (1 << i):
                    curr.append(i - 10)

            res.append(curr)

            mask -= 1
            mask = mask & init


        res.append([])

        return res

