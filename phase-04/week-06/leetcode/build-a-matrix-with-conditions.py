class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rows, cols = defaultdict(list), defaultdict(list)
        for u, v in rowConditions: rows[u].append(v)
        for u, v in colConditions: cols[u].append(v)

        def cycle(node, g, col):
            if col[node-1] == 1: return
            neis, cyc = g[node], False

            for nei in neis:
                if col[nei-1] == 0:
                    cyc = True
                    break
                if col[nei-1] == -1:
                    col[nei-1] = 0
                    temp = cycle(nei, g, col)
                    if temp: 
                        cyc = True
                        break

            col[node-1] = 1
            return cyc

        # this block checks to see if any cycle exists in either
        # the topologically sorted row or column ordering
        colcol = [-1 for _ in range(k)]
        colrow = [-1 for _ in range(k)]
        for i in range(1,k+1):
            if colcol[i-1] == -1:
                colcol[i-1] = 0
                temp = cycle(i, cols, colcol)
                if temp: return [] 

            if colrow[i-1] == -1:
                colrow[i-1] = 0
                temp = cycle(i, rows, colrow)
                if temp: return [] 

        # this block of code contains two functions to topologically sort
        # the row and column orderings
        def dfsrow(node):
            if col[node-1] == 1: return
            neis = rows[node]

            for nei in neis:
                if col[nei-1] == -1:
                    col[nei-1] = 0
                    dfsrow(nei)
                elif col[nei-1] == 0:
                    return

            col[node-1] = 1
            toprow.append(node)

        def dfscol(node):
            if col[node-1] == 1: return
            neis = cols[node]

            for nei in neis:
                if col[nei-1] == -1:
                    col[nei-1] = 0
                    dfscol(nei)
                elif col[nei-1] == 0:
                    return

            col[node-1] = 1
            topcol.append(node)


        col = [-1 for _ in range(k)]
        toprow = []
        for i in range(1,k+1):
            if col[i-1] == -1:
                col[i-1] = 0
                dfsrow(i)

        col = [-1 for _ in range(k)]
        topcol = []
        for i in range(1,k+1):
            if col[i-1] == -1:
                col[i-1] = 0
                dfscol(i)

        topcol.reverse()
        toprow.reverse()

        # this block consructs the matrix and puts the numbers
        # in their appropriate [row][col] position
        ans = [[0 for _ in range(k)] for _ in range(k)]
        inds = dict()

        for ind, node in enumerate(topcol):
            inds[node] = ind

        for i in range(k):
            num = toprow[i]
            ind = inds[num]
            ans[i][ind] = num


        return ans 
