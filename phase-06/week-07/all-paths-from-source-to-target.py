class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        que = deque([(i, "0") for i in graph[0]])
        n = len(graph)
        target = n - 1

        ans = []
        
        while que:
            for _ in range(len(que)):
                curr, path = que.popleft()
                path += "," + str(curr)
                if curr == target:
                    ans.append(list(map(int, path.split(","))))
                for nei in graph[curr]:
                    que.append((nei, path))

        return ans


        
