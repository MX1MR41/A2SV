class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # the greediness of this approach lies in the nature of the partitioning of marbles into bags.
        # if we partition a to c marbles into one bag and d to f marbles the score would be (a + d) + (e + f).
        # if we have another partiotion like a to b in one bag and c to f in another, the score would be 
        # (a + b) + (c + f).
        # if we consider the first as the max and the second as min,
        # our answer would be their difference ((a + d) + (e + f)) - ((a + b) + (c + f))
        # a and f get cancelled out and we remain with d + e - (b + c)
        # so the sole determinants are the the partition points - their sum. 
        # So we compute all partition sums and sort them to greedily get the max and the mins then process those
        if k == 1:
            return 0

        parts = []
        for i in range(len(weights) - 1):
            parts.append(weights[i] + weights[i+1])

        parts.sort()
        
        return sum(parts[-k + 1:]) - sum(parts[:k-1])