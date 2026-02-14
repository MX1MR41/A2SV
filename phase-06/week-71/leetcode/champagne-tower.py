class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp
        # fill up the topmost glass first, then iterate row by row col by col 
        # transferring any extra to the children
        
        if poured == 0:
            return 0

        tree = [[0 for _ in range(i)] for i in range(1, query_row + 3)]
        tree[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                if tree[r][c] > 1:
                    extra = tree[r][c] - 1
                    tree[r + 1][c] += extra/2
                    tree[r + 1][c + 1] += extra/2

        return min(1, tree[query_row][query_glass])

        return 0
