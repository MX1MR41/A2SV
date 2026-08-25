# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def con(nums):
            if not nums:
                return 
            if len(nums) == 1:
                return TreeNode(nums.pop())

            m = max(nums)
            ind = nums.index(m)

            node = TreeNode(m)
            node.right = con(nums[ind+1:])
            node.left = con(nums[:ind])

            return node

        return con(nums)
        