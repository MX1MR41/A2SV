class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # prefix sum
        # while iterating the array and keeping track of the prefix sum,
        # keep count of the odd and even prefix sums seen so far
        # to make an even subarray odd, we deduct an odd subarray from it
        # to make an odd subarray odd, we deduct an even subarray from it
        seen = defaultdict(int)
        seen[0] = 1
        pre = 0
        count = 0
        for i in arr:
            pre += i
            if pre % 2:
                count += seen[0]
                seen[1] += 1
            else:
                count += seen[1]
                seen[0] += 1

        return count % (10**9 + 7)
        
