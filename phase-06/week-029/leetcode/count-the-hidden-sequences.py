class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # interval problem
        # start from the first position and compute the range of possible nums for it
        # then based on it, compute the valid range for the next position.
        # For every next position, compute the range of nums that could be put there if it was 
        # the first position, and compute the intersection of this new range and the range previously
        # decided for this position by its predecessor position. That intersection will be the range
        # for this new position, then compute next position's range fromthis intersection and repeat

        def findRange(k, lower, upper):
            if upper - lower < k:
                return []

            if k >= 0:
                left = lower
                right = upper - k

            else:
                right = upper
                left = lower - k

            return [left, right]


        n = len(differences) + 1

        curr_range = findRange(differences[0], lower, upper)

        if not curr_range:
            return 0

        next_range = [curr_range[0] + differences[0], curr_range[1] + differences[0]]

        for diff in differences[1:]:
            new_range = findRange(diff, lower, upper)

            if (
                not new_range
                or next_range[1] < new_range[0]
                or next_range[0] > new_range[1]
            ):
                return 0

            intersection = [
                max(next_range[0], new_range[0]),
                min(next_range[1], new_range[1]),
            ]

            if intersection[0] > intersection[1]:
                return 0

            curr_range = intersection
            next_range = [curr_range[0] + diff, curr_range[1] + diff]

        return curr_range[1] - curr_range[0] + 1
