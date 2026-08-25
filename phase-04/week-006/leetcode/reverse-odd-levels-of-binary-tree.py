# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # store all nodes by their respective levels and respective order in a dictionary
        # for every level and next level, do a criss-cross stitching

        # storing nodes 
        nodes = defaultdict(list)
        lev = 0
        que = deque([root])
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                    que.append(node.right)

                nodes[lev].append(node)

            lev += 1

        # travel every level
        for i in range(0, lev - 1):
            curr_level = deque(nodes[i])
            nxt_level = deque(nodes[i + 1])

            for _ in range(len(curr_level)):
                node = curr_level.popleft()

                # if it is an even level, we just have to stitch nodes from the lower level
                # in a directly reverse manner
                if not i % 2:
                    node.left = nxt_level.pop()
                    node.right = nxt_level.pop()

                # if it is odd, since this level has been reversed, the nodes from lower level
                # are stitched in a reverse but cross-child manner
                else:
                    node.right = nxt_level.pop()
                    node.left = nxt_level.pop()

        return root
