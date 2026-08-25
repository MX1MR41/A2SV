class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # maps to hold the pos of guards and walls in the format of {row:{col1, col2}}
        g, w = defaultdict(set), defaultdict(set)
        #the original number of cells minus the ones which contain guards and walls 
        cells = m*n - len(guards) - len(walls)
        # set to contain guarded cells
        guarded = set()
        
        for i in guards:
            g[i[0]].add(i[1])

        for i in walls:
            w[i[0]].add(i[1])
        
        for i in range(m):
            for j in range(n):
                # if the cell has a guard, we check in four directions for guarded cells
                if j in g[i]:
                    a,b = i,j # temp counters
                    # we check until we meet the end or a guard or a wall
                    while b < n-1 and b + 1 not in w[a] and b + 1 not in g[a]:
                        if (a, b + 1) not in guarded:
                            b += 1
                            guarded.add((a,b))
                        else: b += 1

                    a,b = i,j
                    while b > 0 and b - 1 not in w[a] and b - 1 not in g[a]:
                        if (a, b - 1) not in guarded:
                            b -= 1
                            guarded.add((a,b))
                        else: b -= 1

                    a,b = i,j
                    while a < m-1 and b not in w[a+1] and b not in g[a+1]:
                        if (a+1, b) not in guarded:
                            a += 1
                            guarded.add((a,b))
                        else: a += 1

                    a,b = i,j
                    while a > 0 and b not in w[a-1] and b not in g[a-1]:
                        if (a-1, b) not in guarded:
                            a -= 1
                            guarded.add((a,b))
                        else: a -= 1

        cells -= len(guarded)
        return cells