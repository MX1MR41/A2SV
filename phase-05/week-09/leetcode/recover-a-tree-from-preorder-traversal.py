# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # stack
        # keep track of the last added nodes for every depth
        # and for every node at depth d, append it as a child to the last node added
        # for depth d - 1, i.e. candidate parent

        travs = []
        curr = ""
        flag = True

        n = len(traversal)
        i = 0
        while i < n:
            if traversal[i] == "-":
                if flag:
                    travs.append(curr)
                    curr = ""
                    flag = False

            else:
                flag = True

            curr += traversal[i]
            i += 1

        if curr:
            travs.append(curr)

        nodes = []
        for trav in travs:
            split = trav.split("-")
            nodes.append((int(split[-1]), len(split) - 1))

        nodes_at_depth = defaultdict(list)
        root = TreeNode(nodes[0][0])
        nodes_at_depth[0].append(root)

        for num, depth in nodes[1:]:
            node = TreeNode(num)
            parent = nodes_at_depth[depth - 1][-1]

            if not parent.left:
                parent.left = node

            else:
                parent.right = node
                nodes_at_depth[depth - 1].pop()

            nodes_at_depth[depth].append(node)

        return root
