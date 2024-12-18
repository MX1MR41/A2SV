class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(node, target, visited):
            if node == target:
                return 1.0
            
            visited.add(node)
            for neighbor, value in graph[node]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1:
                        return result * value
            
            visited.remove(node)  # Backtrack to allow revisiting for other paths
            return -1

        # Evaluate each query
        results = []
        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1.0)
            elif a == b:
                results.append(1.0)
            else:
                results.append(dfs(a, b, set()))

        return results
