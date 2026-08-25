class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tot = 0
        for i in nums:
            tot ^= i

        return str(bin(tot^k)).count("1")
        
