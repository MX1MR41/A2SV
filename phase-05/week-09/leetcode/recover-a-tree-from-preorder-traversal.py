# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # keep track of nodes by using a hashmap with depth as key
        # for each node, attach it to the last node added to the depth just above it
        nodes_at_depth = defaultdict(list)
        i = 0
        n = len(traversal)
        depth = 0

        while i < n:
            if traversal[i] == "-": 
                depth += 1
                i += 1
            else:
                j = i + 1
                while j < n and traversal[j] != "-": 
                    j += 1
                node = int(traversal[i:j])
                parent_depth = depth - 1

                if not nodes_at_depth[parent_depth]:
                    nodes_at_depth[depth].append(TreeNode(node))
                else:
                    parent = nodes_at_depth[parent_depth][-1]
                    if parent.left:
                        parent.right = TreeNode(node)
                        nodes_at_depth[depth].append(parent.right)
                    else:
                        parent.left = TreeNode(node)
                        nodes_at_depth[depth].append(parent.left)
                
                depth = 0
                i = j
            
        return nodes_at_depth[0].pop()
