# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        M = m = root.val
        def inOrder(M, m, root):
            nonlocal res
            if root:
                curr = root.val
                M, m = max(M, curr), min(m, curr)
                res = max(res, abs(M - curr), abs(m - curr))
                inOrder(M, m, root.left)
                inOrder(M, m, root.right)

        inOrder(M, m, root)
        return res

            

        