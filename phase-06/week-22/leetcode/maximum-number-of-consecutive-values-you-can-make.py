class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # greedy 
        # assume we have a set S of numbers that we know can form all nums up to 7
        # if we add 4 into this set, we can form the nums from 8 to 11 by adding
        # 4, 5, 6, 7 to the new 4. Those nums themselves might not be present in 
        # S but they might be formed by addition of smaller nums.
        # But if we say add 9 onto S, we can't form 8 (the next num) any way
        

        max_consecutive = 1

        for coin in sorted(coins):
            
            # if the current coin is greater than the next max_consecutive
            # we can't form the next max_consecutive and consequently next nums
            if coin > max_consecutive:
                break

            max_consecutive += coin

        return max_consecutive
