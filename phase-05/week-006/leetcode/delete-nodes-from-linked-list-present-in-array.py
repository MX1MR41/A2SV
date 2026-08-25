# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        ans = prev = ListNode()
        curr = head
        prev.next = curr
        while curr:
            if curr.val in nums:
                prev.next = None
                curr = curr.next
            else:
                prev.next = curr
                prev = prev.next
                curr = curr.next

        return ans.next
        
