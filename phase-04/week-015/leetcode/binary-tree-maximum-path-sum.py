class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(head):
            if not head:
                return 0

            left = max(dfs(head.left), 0)
            right = max(dfs(head.right), 0)

            self.max_sum = max(self.max_sum, left + right + head.val)

            return max(left, right) + head.val

        dfs(root)

        return self.max_sum
