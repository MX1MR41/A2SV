class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # topological sort
        # starting from the leaf nodes and summing upwards in a bottom-up fashion guarantees
        # we compute for every node in the most optimal manner

        graph = defaultdict(list)
        degree = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1


        que = deque([i for i in range(n) if degree[i] <= 1])
        components = 0
        visited = set()

        while que:

            for _ in range(len(que)):
                node = que.popleft()
                
                if node in visited: # prevent repetition and cycles
                    continue

                current_sum = values[node]

                visited.add(node)

                # a valid split is found
                if not current_sum % k:
                    components += 1

                for nei in graph[node]:

                    degree[nei] -= 1

                    # sum up the leaf nodes values onto the parent node's value
                    # so it becomes prefix-sum-like 
                    values[nei] += current_sum

                    if degree[nei] <= 1:
                        que.append(nei)

        return components

