class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if either of these two is None, return the one that isnt None
        if not root1:
            return root2

        if not root2:
            return root1

        # if neither are None, then we create a new node with val
        # equal to the sum of the two roots' vals
        # then we recursively do the same for their left and right

        merged = TreeNode(root1.val + root2.val)

        merged.left = self.mergeTrees(root1.left, root2.left)

        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged
