# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        res = []

        def inOrder(root):
            
            if root:
                inOrder(root.left)
                if low <= root.val <= high:
                    res.append(root.val)
                inOrder(root.right)
            

        inOrder(root)
        return sum(res)
        