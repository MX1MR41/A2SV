# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)

        def bfs(que, visited):
            path = 0

            while que:
                if path == k:
                    return list(que)
                    
                for _ in range(len(que)):
                    curr = que.popleft()
                    if curr in visited: continue
                    visited.add(curr)

                    for nei in g[curr]:
                        if nei not in visited: que.append(nei)

                path += 1

        def pre(head):
            if head:
                if head.right:
                    g[head.val].append(head.right.val)
                    g[head.right.val].append(head.val)
                    pre(head.right)

                if head.left:
                    g[head.val].append(head.left.val)
                    g[head.left.val].append(head.val)
                    pre(head.left)

        pre(root)
        ans = bfs(deque([target.val]), set())
        return ans if ans else []
