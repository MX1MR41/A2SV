# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        global x
        x = val

        def inOrder(head):
            if head:
                if head.val == x:
                    return head
                left = inOrder(head.left)
                right = inOrder(head.right)
                if left:
                    return left
                if right:
                    return right

    
        res = inOrder(root)

        return res
        
        