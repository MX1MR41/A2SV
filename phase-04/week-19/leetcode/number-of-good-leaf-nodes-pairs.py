# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # graph-ization + bfs
        # would've worked fine if all nodes were unique, but they werent
        # so i made them 😌
        leaves = set()
        g = defaultdict(list)
        pairs = set()
        
        def dfs(node):
            if node:
                if node.left is None and node.right is None:
                    leaves.add(node.val)

                if node.left:
                    while node.left.val in g:
                        node.left.val += 100
                    g[node.val].append(node.left.val)
                    g[node.left.val].append(node.val)
                    dfs(node.left)
                if node.right:
                    while node.right.val in g:
                        node.right.val += 100
                    g[node.val].append(node.right.val)
                    g[node.right.val].append(node.val)
                    dfs(node.right)

        dfs(root)
        

        def bfs(que, leaf):
            visited = set()
            visited.add(leaf)
            dist = 1
            while que:

                if dist > distance: 
                    break
        
                for _ in range(len(que)):
                    node = que.popleft()
                    if node in visited: continue
                    visited.add(node)
                    que.extend(g[node])
                    if node in leaves and dist <= distance:
                
                        pairs.add(tuple(sorted([leaf, node])))

                dist += 1

        for leaf in leaves:
            bfs(deque(g[leaf]), leaf)

        
        return len(pairs)


         

        
