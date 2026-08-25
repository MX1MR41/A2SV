class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        g = defaultdict(list)

        for i in range(len(edges)):
            g[i].append(edges[i])

        def dfs(node, visited, path):
            # if cycle is found, we iterate backwards in our path list
            # till we find the starting point of the cycle. At the same time we 
            # are counting number of nodes in between i.e. the length of that cycle which we return
            if node in visited: 
                length = 1
                ind = len(path) - 1
                while path[ind] != node:
                    ind -= 1
                    length += 1
                return length

            path.append(node)
            visited.add(node)

            # if a cycle hasn't been found yet, we need to explore further
            # in the adjacency list IF their is an adjacent node
            ans = max(0, dfs(g[node].pop(), visited, path)) if g[node] else 0

            return ans

        cycle = 0
        for i in range(len(edges)):
            cycle = max(cycle, dfs(i, set(), []))

        return cycle if cycle else -1
