# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(roota, rootb):

            if (not roota and not rootb):
                return True

            if (not roota and rootb) or (roota and not rootb):
                return False

            if roota.val != rootb.val:
                return False

            lefta = leftb = righta = rightb = None

            if roota.left: lefta = roota.left.val
            if roota.right: righta = roota.right.val
            if rootb.left: leftb = rootb.left.val
            if rootb.right: rightb = rootb.right.val

            if lefta == leftb and rightb == righta:
                return dfs(roota.right, rootb.right) and dfs(roota.left, rootb.left)
            
            if not lefta and not leftb:
                return dfs(roota.right, rootb.right)
            
            if not righta and not rightb:
                return dfs(roota.left, rootb.left)

          
            rootb.left, rootb.right = rootb.right, rootb.left
            return dfs(roota.right, rootb.right) and dfs(roota.left, rootb.left)


            return True

        return dfs(root1, root2)
            
        
