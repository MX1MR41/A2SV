# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # keep track of the left and right children from the traversals
        
        right = defaultdict(int)
        left = defaultdict(int)
        n = len(preorder)

        # if a nodeB comes after nodeA in the preorder traversal, it could be nodeA's left child
        for i in range(n - 1):
            left[preorder[i]] = preorder[i + 1]


        # if a nodeB comes before nodeA in the postrder traversal, it could be nodeA's right child
        for i in range(n - 1, 0, -1):
            right[postorder[i]] = postorder[i - 1]
        
        # create the root
        root = TreeNode(preorder[0])

        seen = set()
        seen.add(root.val)


        # perform bfs starting from the root node and assigning left and right children as you go
        # starting from the root ensure we process the nodes in the proper order and won't 
        # mismatch any node to a wrong parent
        que = deque([(left[root.val], root, True), (right[root.val], root, False)])

        while que:

            for _ in range(len(que)):
                child_val, parent, leftie = que.popleft()

                # this node has been seen before and is the child of another node, 
                # not this parent's child
                if child_val in seen or child_val == 0:
                    continue

                seen.add(child_val)
                node = TreeNode(child_val)

                # attach to parent
                if leftie:
                    parent.left = node
                else:
                    parent.right = node

                que.append((left[node.val], node, True))
                que.append((right[node.val], node, False))

        return root
