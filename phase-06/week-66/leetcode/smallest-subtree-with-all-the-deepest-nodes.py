# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        max_depth = 0
        nodes_at_depth = defaultdict(list)
        parent = {}
        parent[root] = None
        que = deque([(root, 0)])
        while que:
            for _ in range(len(que)):
                node, d = que.popleft()
                max_depth = max(max_depth, d)
                nodes_at_depth[d].append(node)

                if node.left:
                    que.append((node.left, d + 1))
                    parent[node.left] = node

                if node.right:
                    que.append((node.right, d + 1))
                    parent[node.right] = node

        
        que = deque(nodes_at_depth[max_depth])
        if len(que) == 1:
            return que.pop()
        while que:
            next_lev = set()
            for _ in range(len(que)):
                node = que.popleft()
                par = parent[node]
                next_lev.add(par)

            if len(next_lev) == 1:
                return next_lev.pop()

            que = deque(list(next_lev))




        

        
