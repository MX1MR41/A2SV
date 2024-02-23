# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:
            return True

        if not root.right or not root.left:
            return False


        # modified code from is same-tre problem
        # https://leetcode.com/problems/same-tree/description/
        def func(p, q):
            if not p and not q:
                return True
        
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return func(p.left, q.right) and func(p.right, q.left)

        return func(root.right, root.left)


        