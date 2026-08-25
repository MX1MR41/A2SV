class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # dfs
        # in any given tree, the nodes can be grouped into two groups, where for a given group
        # all the nodes in that group will have the same (odd_distanced_nodes, even_distanced_nodes)
        # that is because every tree is bipartite. So once we perform dfs on a single node to compute
        # the (odd_distanced_nodes, even_distanced_nodes) from that source node, we assign this result
        # to all the nodes in the the same bipartite group as the source node from which we did dfs.
        # The grouping can be done within the dfs.
        # To compute the (odd, even) of a node, it is going to be (even + 1, odd) of its neighbor
        # because the parity keeps swapping at each move, and +1 to account for the edge between them\.
        # After computing this for both trees and grouping the nodes in both trees, 
        # the new edge options that we have from a node in tree1 is to either group of tree2

         

        def dfs(node, g, seen, flag, f):
            odd = even = 0

            seen.add(node)
            flag[node] = f

            for nei in g[node]:
                if nei not in seen:
                    new_odd, new_even = dfs(nei, g, seen, flag, not f)
                    odd += new_odd
                    even += new_even

            return even + 1, odd


        g1 = defaultdict(list)
        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)

        g2 = defaultdict(list)
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)

        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        flag1 = dict()
        even1, odd1 = dfs(0, g1, set(), flag1, True)

        flag2 = dict()
        even2, odd2 = dfs(0, g2, set(), flag2, True)

        choices = [[odd2, even2], [even2, odd2]]

        ans = []

        for i in range(n1):
            if flag1[i]:
                curr_odd, curr_even = odd1, even1
            else:
                curr_odd, curr_even = even1, odd1

            curr = 0

            for o, e in choices:
                curr = max(curr, curr_even + o)

            ans.append(curr)

        return ans
