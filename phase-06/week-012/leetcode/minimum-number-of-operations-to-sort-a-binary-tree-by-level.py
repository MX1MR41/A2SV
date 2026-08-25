# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # bfs + sorting
        # to calculate minimum number of swaps to sort an array, make a sorted copy
        # then while iterating the array if the num differs from the sorted copy,
        # swap with the number that is supposed to be there. Keeping track of indices and
        # updating  them dynamically helps.
        def swaps(arr):
            swap = 0
            arr = [[num, ind] for ind, num in enumerate(arr)]
            ordered = sorted(arr)

            for i in range(len(arr)):
                while arr[i][0] != ordered[i][0]:
                    ind1, ind2 = arr[i][1], ordered[i][1]
                    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]
                    arr[ind1][1], arr[ind2][1] = ind1, ind2
                    swap += 1

            return swap

        res = 0
        que = deque()
        if root.left:
            que.append(root.left)
        if root.right:
            que.append(root.right)

        while que:
            arr = [node.val for node in que]
            res += swaps(arr)
            for _ in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return res

        
