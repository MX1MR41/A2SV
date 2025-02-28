class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # dp
        # for every number z, for every other number y before it, you will find a number x = z - y
        # such that x occurs before y
        # and the length of the sequnce from x to z would be the length of the sequence from x to y
        # plus 1 for z.

        index = {num: i for i, num in enumerate(arr)}
        dp = defaultdict(lambda : 2)  # base case is 2, any two numbers can be the first in fib seq
        res = 0
        
        for j in range(len(arr)):
            third = arr[j]
            for i in range(j):
                second = arr[i]
                first = third - second  

                if first in index and index[first] < i:  
                    k = index[first]

                    dp[(i, j)] = dp[(k, i)] + 1

                    res = max(res, dp[(i, j)])

        return res if res >= 3 else 0  
