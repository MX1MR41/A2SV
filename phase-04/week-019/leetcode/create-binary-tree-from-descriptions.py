# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # enumerate all nodes, find out the root node, build the tree

        has_parent = defaultdict(bool) # False if root node
        all_nodes = set() # store all nodes
        child = defaultdict(lambda: [0, 0]) # stores left and right children

        for par, ch, left in descriptions:
            all_nodes.add(par)
            all_nodes.add(ch)
            has_parent[ch] = True

            if left: child[par][0] = ch
            else: child[par][1] = ch

        # finding the root node
        for node in all_nodes:
            if not has_parent[node]:
                root_val = node
                break
        
        # builds tree recursively
        def build(node):
            curr = TreeNode(node)
            left, right = child[node]
            if left:
                curr.left = build(left)
            if right:
                curr.right = build(right)

            return curr

        tree = build(root_val)
        return tree


