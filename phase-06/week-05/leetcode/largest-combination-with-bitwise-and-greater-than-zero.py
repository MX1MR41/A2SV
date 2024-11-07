class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # for a cumulative AND of numbers to be greater than 1, they must have
        # at least one common set bit
        # so count the total frequency of being set for all bits upto 31'st bit,
        # then return the max freqency
        bits = [0]*32

        for cand in candidates:
            mask = str(bin(cand))[2:]
            mask = mask[::-1]

            for i in range(len(mask)):
                if mask[i] == "1":
                    bits[i] += 1


        return max(bits)
        
