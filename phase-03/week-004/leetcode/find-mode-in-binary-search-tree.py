# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inOrder(head):
            if head:
                inOrder(head.left)
                res.append(head.val)
                inOrder(head.right)

        inOrder(root)

        cnt = Counter(res)
        m = 0
        for i in cnt:
            m = max(m, cnt[i])

        ans = []
        for i in res:
            if cnt[i] == m and i not in ans:
                ans.append(i)

        return ans
        