# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    
        
        ans = None

        def div(arr):
            n = len(arr)
            if not n:
                return

            ind = n//2

            new = TreeNode(arr[ind])
            new.right = div(arr[ind+1:])
            new.left = div(arr[:ind])

            return new

        
        ans = div(nums)

        return ans

        