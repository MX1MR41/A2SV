# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # dfs + reverse bfs + dp
        # Overall solved by first solving the base-cases which are the nodes at the lowest level
        # and using their info to dynamically build up the solutions for upper levels level by level.

        # At each level, we'll have the dynamically built depth of going through a node for all nodes
        # of the same level. From these depths, get the maximum and its frequency. If its singular,
        # assign every other node's dynamic depth to this maximum, and assign the max node's depth as
        # the second maximum. If its plural then assign every node's dynamic depth to the maximum.

        # First do a dfs and store the nodes in a level-by-level manner, record the maximum depth,
        # assign the parent of each node, and initialize their dp values. Then start from the deepest
        # level and perform the operations listed above to dynamically build up the answers.

        
        nodes_at_depth = defaultdict(list)
        parent = dict()
        max_depth = 0
        dp = defaultdict(int)

        def dfs(node, d, p):
            nonlocal max_depth
            if node:
                dp[node.val] = d
                max_depth = max(max_depth, d)
                nodes_at_depth[d].append(node.val)
                parent[node.val] = p

                dfs(node.left, d + 1, node.val)
                dfs(node.right, d + 1, node.val)

        dfs(root, 0, None)

        
        # start from the deepest level
        que = deque(nodes_at_depth[max_depth])

        while que:
            # assign the depth of the children to the parents
            for i in que:
                dp[parent[i]] = max(dp[parent[i]], dp[i])

            # retriev the max depth and its frequency
            temp = [dp[i] for i in que]
            deepest = max(temp)
            cnt = temp.count(deepest)

            # if there is only one node at this level, removing it would overall decrease depth by 1
            if len(temp) == 1:
                dp[que.pop()] = max_depth - 1

            else:
                # since there are multiple max depths, removing any node wouldn't affect the max depth
                if cnt > 1:
                    for i in que:
                        dp[i] = deepest

                # else if the max depth has only one instance
                else:
                    # calculate the second deepest depth
                    second = 0
                    for i in temp:
                        if i < deepest:
                            second = max(second, i)

                    # if the max depth is from this node, removing it would make the answer the second
                    for i in que:
                        if dp[i] == deepest:
                            dp[i] = second
                        else:
                            dp[i] = deepest

            # go up a level
            max_depth -= 1 
            que = deque(nodes_at_depth[max_depth])

        return [dp[i] for i in queries]
