# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # collect nodes in groups of k, then reverse that group
        
        # the dummy node whose next will contain our final modified linked list's head
        last_end = dummy = ListNode()

        # we start from the head
        curr_start = head 

        while True:
            curr_end = curr_start
            nodes = 1
            
            # move curr_end to the kth node from curr_start
            while curr_end and nodes < k:
                curr_end = curr_end.next
                nodes += 1

            # if there are k nodes that we can reverse
            if nodes == k and curr_end:

                next_start = curr_end.next # store it in a temporary variable for later
                
                # start and end of the modified list
                start, end = self.reverse(curr_start, curr_end)

                last_end.next = start # attach the start to the last group's end

                last_end = end # store the current end as "last_end" for the next group

                curr_start = next_start # get the next start that we previously stored

            # if we don't have at leat k nodes remaining, just attach it to the last_end 
            else:
                last_end.next = curr_start
                break

        return dummy.next

    def reverse(self, start, end):
        # separate function to reverse a linked list given its start and end
        prev = None
        curr = start

        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        end.next = prev

        return end, start
