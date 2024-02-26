# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = []
        curr = ""
        def preOrder(curr, head):
            if head:
                curr += str(head.val)
                if not head.right and not head.left:
                    res.append(curr)

                if head.right:
                    preOrder(curr, head.right)

                if head.left:
                    preOrder(curr, head.left)

        preOrder(curr, root)
        ans = 0
        for i in res:
            ans += int(i)
        return ans


        