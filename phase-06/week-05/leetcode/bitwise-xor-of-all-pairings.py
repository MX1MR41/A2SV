class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = len(nums1), len(nums2)

        tot1 = tot2 = 0
        for i in nums1:
            tot1 ^= i

        for j in nums2:
            tot2 ^= j

        # if both are even then total xor will be 0 since each number will occur even times
        if not n1 % 2 and not n2 % 2:
            return 0
        # if both are odd then total xor will be xor of the two since every num will occur odd times
        elif n1 % 2 and n2 % 2:
            return tot1 ^ tot2
        # if n1 is odd but n2 is even, n1 elements will occur evenly and n2 elements will occur oddly
        elif n1 % 2:
            return tot2
        else:
            return tot1
        
