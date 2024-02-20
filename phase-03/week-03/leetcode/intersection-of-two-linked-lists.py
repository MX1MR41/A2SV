# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = [], []
        dummyA = headA
        while dummyA:
            A.append(dummyA)
            dummyA = dummyA.next

        dummyB = headB
        while dummyB:
            B.append(dummyB)
            dummyB = dummyB.next


        last = None
        a, b = len(A)-1, len(B)-1 # two pointers to iterate backwards
        while a >= 0 and b >= 0 and A[a] == B[b]:
            last = A[a]
            a -= 1
            b -= 1

        return last