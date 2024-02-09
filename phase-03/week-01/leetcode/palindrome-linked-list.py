class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
    
        while fast and fast.next: # slow will point to the middle at the end of the loop
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow: # reverse the list from slow to the end
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        l, r = head, prev # left and right pointers to check if palindrome or not
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
            
        return True
        