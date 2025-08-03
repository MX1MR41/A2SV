class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # prefix sum + sliding window
        # consider the different possible configurations of movement and use prefix sum to compute
        # the sum of fruits over distances

        n = max(fruits[-1][0], startPos) + 1
        axis = [0] * (n)

        for pos, fr in fruits:
            axis[pos] = fr

        prefix = axis[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        # edge case
        if startPos == 0:
            return prefix[min(startPos + k, n - 1)]

        res = 0

        # moving to the left first and moving back to the right if extra moves remain
        for i in range(startPos + 1):
            diff = startPos - i
            if diff > k:
                continue
            
            # to the left of startPos
            left = prefix[startPos] - prefix[i - 1] if i - 1 >= 0 else prefix[startPos]

            # to the right of startPos
            right = 0

            # we can still move back and beyond startPos
            if 2 * diff < k:
                remaining = k - (2 * diff)
                right = prefix[min(startPos + remaining, n - 1)] - prefix[startPos]

            res = max(res, left + right)
        

        # moving to the right first and moving back to the left in any moves remain
        for i in range(startPos + 1, n):
            diff = i - startPos
            if diff > k:
                continue

            right = prefix[i] - prefix[startPos - 1] if startPos - 1 >= 0 else prefix[i]
            left = 0
            if 2 * diff < k:
                remaining = k - (2 * diff)
                ind = startPos - remaining - 1
                left = (
                    prefix[startPos - 1] - prefix[ind]
                    if ind >= 0
                    else prefix[startPos - 1]
                )

            res = max(res, left + right)

        return res
