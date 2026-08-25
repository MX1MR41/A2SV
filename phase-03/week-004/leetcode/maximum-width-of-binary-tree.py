class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # modified code from Vertical Order Traversal of a Binary Tree
        # https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
        rows = defaultdict(list)
        
        # this function store all nodes along with their column indices
        # the nodes are grouped by their respective rows
        def dfs(head, r, c):
            if head:
                rows[r].append([c, head.val])
                if head.left:
                    # since the width of children will be twice the parent
                    # we pass twice the column index 
                    dfs(head.left, r + 1, c * 2)
                if head.right:
                    # we do the same for the right too but with a small differenece
                    # we add 1, to maintain the notion that the width between the 
                    # right and left child of a given node is 1
                    dfs(head.right, r + 1, c * 2 + 1)
                
        dfs(root, 0, 0)
        
        res = 0
        for row, nodes in rows.items():
            # we need to sort them by their column indices
            nodes.sort(key=lambda x: x[0])
            # after sorting, the width of that level would be 
            # the column index of the rightmost - column index of leftmost
            res = max(res, nodes[-1][0] - nodes[0][0] + 1)
            
        return res

        
