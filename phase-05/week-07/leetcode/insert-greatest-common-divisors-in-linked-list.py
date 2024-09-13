# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next is None:
            return head

        curr = prev = head
        curr = curr.next

        while curr:
            new = ListNode(gcd(prev.val, curr.val))
            prev.next = new
            new.next = curr
            prev = curr
            curr = curr.next

        return head
        
