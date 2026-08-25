# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
    
        # Move prev to the node before the left position
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse the nodes from left to right
        curr = prev.next
        for _ in range(right - left):
            next_node = curr.next # save the next node
            curr.next = next_node.next # skip the next node and point to its next
            next_node.next = prev.next # make the next node point backwards
            prev.next = next_node # make the next node right next to the first one
        
        return dummy.next
