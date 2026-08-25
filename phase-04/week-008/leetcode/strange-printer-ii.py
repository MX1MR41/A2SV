class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        # we can model the coloring order of the grid as a directed graph
        # where a node points to a node that is colored on top of it 
        # then we check if any cycle exists in our graph, in which case it is impossible 
        # to color the targetGrid
        M, N = len(targetGrid), len(targetGrid[0])
        g = defaultdict(set)
        nums, cols = set(), defaultdict(int)
        
        for i in range(M):
            for j in range(N):
                col = targetGrid[i][j]
                nums.add(col) # enumerating the number of colors for later

                if col not in g: # hasnt been processed yet
                    min_i = max_i = i # the min and max row index of this certain color
                    min_j = max_j = j # min and max column index

                    # iterate through the whole grid to get the correct min, max indices
                    for r in range(M):
                        for c in range(N):
                            new_col = targetGrid[r][c]
                            if new_col == col:
                                min_i, max_i = min(min_i, r), max(max_i, r)
                                min_j, max_j = min(min_j, c), max(max_j, c)

                    # we consider the area from [min_i, min_j] to [max_i, max_j] 
                    # to have been originally colored by col. And if we find any other 
                    # color in that area, that means the new color new_col was colored
                    # on top of the original col. So we draw an edge col -> new_col
                    for r in range(min_i, max_i + 1):
                        for c in range(min_j, max_j + 1):
                            new_col = targetGrid[r][c]
                            if new_col != col: g[col].add(new_col)

        # cycle detector
        def dfs(node):
            if cols[node] == -1: return True

            cols[node] = -1
            neis = g[node]

            for nei in neis:
                temp = dfs(nei)
                if temp: return True

            cols[node] = 1

        for num in nums:
            temp = dfs(num)
            if temp: # a cycle exists, hence impossible to color targetGrid as given 
                return False

        return True


        

        
