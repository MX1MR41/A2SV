class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # greedy
        
        inds = {num:ind for ind, num in enumerate(row)}

        n = len(row)

        swaps = 0
        res = n

        for i in range(0, n, 2):
            a = row[i]
            if a % 2:
                if row[i + 1] != a - 1:
                    swaps += 1
                    ind = inds[a - 1]
                    row[ind], row[i + 1] = row[i + 1], row[ind]
                    inds[row[ind]] = ind
                    inds[row[i + 1]] = i + 1

            else:
                if row[i + 1] != a + 1:
                    swaps += 1
                    ind = inds[a + 1]
                    row[ind], row[i + 1] = row[i + 1], row[ind]
                    inds[row[ind]] = ind
                    inds[row[i + 1]] = i + 1

        return swaps        
