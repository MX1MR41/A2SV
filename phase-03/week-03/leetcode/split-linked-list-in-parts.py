# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res, nodes = [], 0 # the result and the number of nodes (length of list)
        curr = head

        while curr:
            nodes += 1
            curr = curr.next

        # the first part and the remaining parts
        part, left = nodes // k, nodes % k
        curr = head
        prev = None

        for i in range(k):
            res.append(curr)
            for _ in range(part):
                if curr:
                    prev = curr
                    curr = curr.next

            if left and curr:
                prev = curr
                curr = curr.next
                left -= 1

            if prev:
                prev.next = None

        return res                      
        