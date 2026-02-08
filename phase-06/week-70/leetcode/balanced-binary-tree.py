# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(node) -> [bool, int]:
            if not node:
                return True, 0

            balanced = 0
            lh = rh = 0

            if node.right:
                b, rh = check(node.right)
                if not b:
                    return False, rh

                

            if node.left:
                b, lh = check(node.left)

                if not b:
                    return False, lh

            balanced = abs(lh - rh) <= 1

            return balanced, max(lh, rh) + 1

        return check(root)[0]


        
