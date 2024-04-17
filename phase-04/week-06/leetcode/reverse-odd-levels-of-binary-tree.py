# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(que):
            lev = 0

            while que:
                if lev % 2:
                    temp = list(que)
                    vals = [node.val for node in temp]
                    for node in temp:
                        node.val = vals.pop()

                for _ in range(len(que)):
                    node = que.popleft()
                    if node.left:
                        que.append(node.left)
                        que.append(node.right)

                lev += 1

        bfs(deque([root]))

        return root
