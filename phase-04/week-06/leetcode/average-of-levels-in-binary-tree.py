# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []

        def bfs(que, visited):
            while que:
                ans.append(sum([node.val for node in que])/len(que))

                for _ in range(len(que)):
                    node = que.popleft()
                    if node in visited: continue
                    visited.add(node)

                    if node.left: que.append(node.left)
                    if node.right: que.append(node.right)

        bfs(deque([root]), set())

        return ans
        
