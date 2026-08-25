class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # solution works updating the list of ancestors of every node by traversing
        # the nodes in a topologically sorted manner. 
        # we start with a queue with the nodes that have no ancestors, and for all their
        # descendants, we add them into the list of ancestors of their descendants. We also add
        # all ancestors of a current node into the ancestors list of the descendant nodes
        n = numCourses
        indeg = [0] * n
        g = defaultdict(list)
        ancestors = defaultdict(set)

        for pre, course in prerequisites:
            g[pre].append(course)
            indeg[course] += 1

        que = deque()
        for i in range(n):
            # a primordial ancestor
            if indeg[i] == 0:
                que.append(i)

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                neis = g[node]
                for nei in neis:
                    ancestors[nei].add(node)
                    ancestors[nei] = ancestors[nei].union(ancestors[node])
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        que.append(nei)

        res = []

        for pre, course in queries:
            if pre in ancestors[course]:
                res.append(True)
            else:
                res.append(False)

        return res


        
        
        
