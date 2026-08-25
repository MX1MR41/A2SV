# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        level = defaultdict(set)
        depth = 0

        def right(head, lev):
            nonlocal depth
            if head:
                depth = max(depth, lev)

                if not level[lev]:
                    level[lev].add(head.val)

                right(head.right, lev + 1)
                right(head.left, lev + 1)

        right(root, 0)
  

        for i in range(depth + 1):
            print(level[i])
            if level[i]:
                ans.append(level[i].pop())
        return ans
        
