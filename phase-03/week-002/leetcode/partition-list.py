# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0) # temp list for elems less than x
        more = ListNode(0) # temo list for elems greater than x
        dless = less # dummmy pointer for less list
        dmore = more # dummy pointer for more list
        dummy = head # dummy for original list

        while dummy:
            val = dummy.val
            if val < x:
                new = ListNode(val)
                dless.next = new
                dless = dless.next
            else:
                new = ListNode(val)
                dmore.next = new
                dmore = dmore.next

            dummy = dummy.next
            
        dless.next = more.next

        return less.next