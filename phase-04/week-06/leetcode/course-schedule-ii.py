class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        res = []

        for course, pre in prerequisites:
            g[pre].append(course)

        col = [-1 for _ in range(numCourses)]
        # function to check if a cycle exists in graph
        def cycle(node):
            if col[node] == 1: return

            neis = g[node]
            cyc = False

            for nei in neis:
                if col[nei] == 0:
                    cyc = True
                    break

                if col[nei] == -1:
                    col[nei] = 0
                    temp = cycle(nei)
                    if temp: 
                        cyc = True
                        break

            col[node] = 1

            return cyc

        # pre-check to see if a cycle exists in the graph
        # in that case we return an empty list
        for i in range(numCourses):
            if col[i] == -1:
                col[i] = 0
                temp = cycle(i)
                if temp: return [] 


        col = [-1 for _ in range(numCourses)]

        def dfs(node):
            if col[node] == 1:
                return

            neis = g[node]

            for nei in neis:
                if col[nei] == -1:
                    col[nei] = 0
                    dfs(nei)
                elif col[nei] == 0:
                    return

            col[node] = 1

            res.append(node)

        
        for i in range(numCourses):
            if col[i] == -1:
                col[i] = 0
                dfs(i)

        return res[::-1]




        
        
