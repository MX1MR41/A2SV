# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        if not head:
            return 

        arr = []
        dummy = head
        
        while dummy:
            arr.append([dummy.val,dummy])
            dummy = dummy.next

        arr.sort(key = lambda x : x[0])

        n = len(arr)
        head = arr[0][1]
        for i in range(n-1):
            n1, n2 = arr[i], arr[i+1]
            n1[1].next = n2[1]

        arr[-1][1].next = None

        return head

        