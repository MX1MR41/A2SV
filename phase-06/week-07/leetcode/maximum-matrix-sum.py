class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # *if you can swap elements, you can sort them in any way*
        # that way we can move all negative numbers so they are adjacent to each other
        # and if we have even number of negative nums, we can make them all positive
        # but if odd, we must leave one negative number because it can't be paired up
        # since we can make any number negative instead of it, we choose the smallest
        # absolute value num to be that one negative number that would minimize the
        # deduction from the total sum
        n = len(matrix)
        negatives = 0
        min_val = float("inf")
        total = 0
        for row in matrix:
            for num in row:
                total += abs(num)
                min_val = min(min_val, abs(num))
                if num < 0:
                    negatives += 1

        if negatives % 2 == 0:
            return total
        else:
            return total - 2*min_val
