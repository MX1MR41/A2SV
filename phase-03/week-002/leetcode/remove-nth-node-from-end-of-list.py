class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        
        for _ in range(n):
            if not right:  
                return head
            right = right.next

        if not right:  
            return head.next  

        left = head
        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return head
