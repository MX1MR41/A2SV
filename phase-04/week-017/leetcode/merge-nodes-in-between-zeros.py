# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_res = res = ListNode()
        curr = 0

        dummy = head.next

        while dummy:
            if dummy.val == 0:
                dummy_res.next = ListNode(curr)
                dummy_res = dummy_res.next
                curr = 0

            curr += dummy.val
            dummy = dummy.next

        return res.next

