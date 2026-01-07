# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # bfs + topological sorting
        # move from leaves to upwards while summing up a subtree's sum
        # then calculating the remaining sum, then multiplying those two sums

        parent = {}
        parent[root] = None
        deg = defaultdict(int)
        que = deque([root])
        total = 0

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                total += node.val
                if node.left:
                    parent[node.left] = node
                    que.append(node.left)

                    deg[node] += 1
                    deg[node.left] += 1

                if node.right:
                    parent[node.right] = node
                    que.append(node.right)

                    deg[node] += 1
                    deg[node.right] += 1

        que = deque()
        for node in deg:
            if deg[node] == 1:
                que.append(node)

        res = 0
        MOD = 10**9 + 7
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                curr_sum = node.val
                rem_sum = total - curr_sum
                curr = curr_sum * rem_sum
                res = max(res, curr)

                par = parent[node]
                if par is None:
                    continue

                par.val += node.val
                deg[par] -= 1
                if deg[par] <= 1:
                    que.append(par)


        return res % MOD



        

        
