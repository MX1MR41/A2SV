# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # do dfs on the tree and if the current node you are visiting needs to be deleted,
        # you do not return it back to its parent to be re-attached (you detach it)

        ans = []
        delete = set(to_delete)

        def trav(node):
            nonlocal ans
            if node:
                if node.val in delete:
                    left = trav(node.left) # none if either empty or to node.left needs to be deleted
                    right = trav(node.right)
                    # if node.left wasn't deleted, we need to add it as its own tree
                    # since its parent was deleted
                    if left: 
                        ans.append(left)
                    if right:
                        ans.append(right)

                    # returns None by defualt indicating deletion

                else:
                    node.left = trav(node.left)
                    node.right = trav(node.right)

                    return node

        root = trav(root)
        if root: # in case the root itself wasn't deleted, we need to count it too
            ans.append(root)

        return ans

        
