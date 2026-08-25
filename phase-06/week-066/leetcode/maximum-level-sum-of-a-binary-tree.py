# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        self.level_sum = defaultdict(int)
        self.max_level = 0

        def dfs(node, level):
            if node:
                self.level_sum[level] += node.val
                self.max_level = max(self.max_level, level)

                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 1)
        max_sum = max(self.level_sum.values())


        for i in range(1, self.max_level + 1):
            if self.level_sum[i] == max_sum:
                return i


        


        
