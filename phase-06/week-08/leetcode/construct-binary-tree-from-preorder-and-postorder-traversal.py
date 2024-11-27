# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # in the preorder array, the previous element could be the parent of the current element if
        # it appears before the previous element in the postorder array

        # in the postorder array, the next element could the the parent of the current element if
        # it appears after the next element in the preorder AND it isn't already a left child
        
        nodes = dict() # reference to the nodes created by the unique values

        for i in range(len(preorder)):
            curr = preorder[i]
            currnode = TreeNode(curr)
            nodes[curr] = currnode

            if i == 0:
                root = currnode
                continue

            prev = preorder[i-1]
            prevnode = nodes[prev]

            if postorder.index(prev) > postorder.index(curr):
                prevnode.left = currnode


        for i in range(len(postorder) - 2, -1, -1):
            nxt = postorder[i + 1]
            nxtnode = nodes[nxt]

            curr = postorder[i]
            currnode = nodes[curr]
            if  preorder.index(nxt) < preorder.index(curr) and currnode is not nxtnode.left:
                nxtnode.right = currnode

        return root
                



        return construct(preorder)


            
