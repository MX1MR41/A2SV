class Solution(object):
    def deleteDuplicates(self, head):
        if not head: 
            return head
        dummy = head

        seen = set()
        seen.add(dummy.val)
        
        while dummy and dummy.next:
            prev = dummy
            curr = prev.next
            val = curr.val
            if val in seen:
                prev.next = curr.next
            else:
                dummy = dummy.next

            seen.add(val)

        return head


        

        
            