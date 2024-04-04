class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # iterative approach
        n = len(graph)
        colors = [0 for _ in range(n)]

        for i in range(n):
            if colors[i] != 0:  
                continue

            stack = [(i, 1)]  
            while stack:
                node, col = stack.pop()
                if colors[node] != 0:  
                    if colors[node] != col:  
                        return False
                    continue

                colors[node] = col
                next_col = -col  
                for neighbor in graph[node]:
                    stack.append((neighbor, next_col))

        return True





class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # recursive approach
        n = len(graph)
        # assign all nodes as black to indicate that they havent been visited yet
        # 1 represents red and -1 represents blue
        colors = [0 for _ in range(n)]
        # we pass the current node along with the color it MUST be and visited set
        def dfs(node, col, visited):
            if node in visited:
                if colors[node] != col: return False # a color it shouldnt be
                return True

            visited.add(node)
            colors[node] = col

            for i in graph[node]:
                # pass -col to make all children have different color than parent
                temp = dfs(i, -col, visited)
                if not temp: return False # bipartition validity failed

            return True # we good

        visited = set()
        # since some componenets can be disconnected, we have iterate with a loop
        for i in range(n):
            # if this node hasnt been visited it means that it is a start node
            # or a disconnected component 
            if i not in visited:
                colors[i] = 1
                temp = dfs(i, -1, visited)
                if not temp: return False

        return True
        
