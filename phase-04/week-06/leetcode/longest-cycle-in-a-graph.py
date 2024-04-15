class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        g = defaultdict(list)
        for i in range(len(edges)):
            g[i].append(edges[i])

        def dfs(node, visited, path):
            if node in visited:
                res = 1
                i = len(path) - 1
                while path[i] != node:
                    i -= 1
                    res += 1
                return res

            path.append(node)
            visited.add(node)

            ans = max(0, dfs(g[node].pop(), visited, path)) if g[node] else 0

            return ans

        cycle = 0
        for i in range(len(edges)):
            cycle = max(cycle, dfs(i, set(), []))

        return cycle if cycle else -1
