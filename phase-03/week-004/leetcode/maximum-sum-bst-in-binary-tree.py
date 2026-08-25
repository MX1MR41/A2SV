class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(head):
            nonlocal res

            if not head:
                return (True, float('inf'), float('-inf'), 0)
            
            # flags of validity, min value, max value and sums of either subtrees
            leftFlag, leftMin, leftMax, leftTot = dfs(head.left)
            rightFlag, rightMin, rightMax, rightTot = dfs(head.right)
            
            # the subtrees are valid
            if leftFlag and rightFlag and leftMax < head.val < rightMin:
                tot = leftTot + rightTot + head.val
                res = max(res, tot)

                return (True, min(leftMin, head.val), max(rightMax, head.val), tot)
            
            return (False, 0, 0, 0)
        
        dfs(root)

        return res
