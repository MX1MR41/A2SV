# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        cnt = defaultdict(list)

        def preOrder(d, head):
            if head:
                cnt[d].append(head.val)
                preOrder(d+1, head.left)
                preOrder(d+1, head.right)

        preOrder(1, root)

        ans = []
        rev = False
        for ind, arr in cnt.items():
            if rev:
                ans.append(arr[::-1])
                rev = False
            else:
                ans.append(arr[:])
                rev = True

        return ans


        