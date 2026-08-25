# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []

        def inOrder(head):
            if head:
                inOrder(head.left)
                res.append(head.val)
                inOrder(head.right)

    
        inOrder(root)

        n = len(res)
        for i in range(1,n):
            if res[i] <= res[i-1]:
                return False
        
        return True