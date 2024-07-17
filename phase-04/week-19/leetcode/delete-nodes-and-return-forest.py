# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        ans = []
        delete = set(to_delete)

        def trav(node):
            nonlocal ans
            if node:
                if node.val in delete:
                    left = trav(node.left)
                    right = trav(node.right)

                    if left: ans.append(left)
                    if right: ans.append(right)

                else:
                    node.left = trav(node.left)
                    node.right = trav(node.right)

                    return node

        root = trav(root)
        if root: ans.append(root)

        return ans
