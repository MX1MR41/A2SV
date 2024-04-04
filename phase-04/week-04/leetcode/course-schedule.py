class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # -1 for white, 0 for gray and 1 for black
        # start with all node as white, meaning unvisited and unexplored yet
        color = [-1 for _ in range(numCourses)]
        # construct the graph
        for course, pre in prerequisites:
            graph[pre].append(course)

        def dfs(node):
            if color[node] == 1: return False # a visited and explored node
            # a visisted yet STILL being explored node, hence a cycle found
            if color[node] == 0: return True 
        
            color[node] = 0 # it is being explored

            for nei in graph[node]:
                temp = dfs(nei)
                if temp: return True

            color[node] = 1
        # there might be disconnected components 
        for node in range(numCourses):
            temp = dfs(node)
            if temp: return False

        return True

        

        
