class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # modified code from Convert Sorted Array into Binary Search Tree
        # https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
        
        # this block of code store all nodes' values and sorts them
        res = []
        def inOrder(head):
            if head:
                inOrder(head.left)
                res.append(head.val)
                inOrder(head.right)
        inOrder(root)
        res.sort()

        # this block of code constructs a BST using a divide-and-conquer method
        def div(arr):
            n = len(arr)
            if not n:
                return
            ind = n//2
            new = TreeNode(arr[ind])
            new.right = div(arr[ind+1:])
            new.left = div(arr[:ind])
            return new

        
        return div(res)
        