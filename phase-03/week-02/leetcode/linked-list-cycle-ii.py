class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow: # when they meet this time, it means there is a cycle
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next

                return slow # the node where they will meet this time is the entrance of the cycle

        return None # if there is no cycle
        