# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # traverse and enumerate then use bfs
        
        L, R, U = defaultdict(int), defaultdict(int), defaultdict(int)
        
        def trav(node):
            if node.left:
                L[node.val] = node.left.val
                U[node.left.val] = node.val
                trav(node.left)
            if node.right:
                R[node.val] = node.right.val
                U[node.right.val] = node.val
                trav(node.right)

        trav(root)
        
        que = deque([(startValue, "")])
        seen = set()
        while que:
            for _ in range(len(que)):
                node, path = que.pop()
                if node == destValue:
                    return path
                if node in seen: continue
                seen.add(node)

                left, right, up = L[node], R[node], U[node]
                if left:
                    que.append((left, path + "L"))
                if right:
                    que.append((right, path + "R"))
                if up:
                    que.append((up, path + "U"))


        return ""

        
