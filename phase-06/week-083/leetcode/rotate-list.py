# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find the new head node via modulo
        # then change the next pointers of the node before it and the tail node

        if k == 0 or head is None:
            return head

        n = 0
        dummy = tail = head
        node_at_ind = {}

        while dummy:
            node_at_ind[n] = dummy
            tail = dummy
            n += 1
            dummy = dummy.next


        rot = k % n
        if rot == 0:
            return head



        new_head_ind = n - rot 
        tail.next = head

        curr = node_at_ind[new_head_ind]

        prev = node_at_ind[new_head_ind - 1]
        prev.next = None

        return curr

        
