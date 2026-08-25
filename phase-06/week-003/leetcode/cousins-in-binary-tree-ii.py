# Custom definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.childsum = 0

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # first accumulate sums of each level, and the sum of the direct children for each parent
        # next modify node values by assigning them difference between their level's sum and parent's 


        level_sum = defaultdict(int)

        def accumulate(head, lev):
            l = r = 0
            if head.left:
                l += accumulate(head.left, lev + 1)
            if head.right:
                r += accumulate(head.right, lev + 1)

            head.childsum = l + r
            level_sum[lev] += head.val

            return head.val

        accumulate(root, 1)


        def modify(head, lev, parentsum):
            head.val = level_sum[lev] - parentsum
            if head.left:
                modify(head.left, lev + 1, head.childsum)
            if head.right:
                modify(head.right, lev + 1, head.childsum)

        modify(root, 1, 0)
        root.val = 0


        return root


        
