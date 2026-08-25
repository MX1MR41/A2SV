# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sum = defaultdict(int)
        
        def dfs(head, lev):
            
            if head:
                level_sum[lev] += head.val

                dfs(head.right, lev + 1)
                dfs(head.left, lev + 1)

        dfs(root, 1)

        if len(level_sum) < k:
            return -1

        return sorted(level_sum.values(), reverse = True)[k-1]
        
