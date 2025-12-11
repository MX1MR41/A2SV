class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # compute the min and max col values for each row
        # as well the min and max row values for each col
        # then for each building, just check if its col value is in between the min and max
        # of its row value; and check if its row value is in between the min and max of its col value
        per_column = defaultdict(lambda : [float("inf"), float("-inf")])
        per_row = defaultdict(lambda : [float("inf"), float("-inf")]) 

        for r, c in buildings:
            per_column[c][0] = min(per_column[c][0], r)
            per_column[c][1] = max(per_column[c][1], r)

            per_row[r][0] = min(per_row[r][0], c)
            per_row[r][1] = max(per_row[r][1], c)

        res = 0

        for r, c in buildings:
            if per_row[r][0] < c < per_row[r][1] and per_column[c][0] < r < per_column[c][1]:
                res += 1

        return res

        
