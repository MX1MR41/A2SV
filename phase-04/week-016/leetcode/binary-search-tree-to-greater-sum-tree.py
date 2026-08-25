# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inOrder(head):
            if head:
                inOrder(head.left)
                nodes.append(head.val)
                inOrder(head.right)

        nodes = []
        inOrder(root)
        nodes.reverse()

        suff, p, d = [0], 0, dict()
        # find the suffix sum of each node.val and store it in a dictionary
        for i in nodes:
            d[i] = suff[-1]
            p += i
            suff.append(p)

        

        def change(head):
            if head:
                head.val += d[head.val]
                change(head.left)
                change(head.right)

        change(root)


        return root
        
