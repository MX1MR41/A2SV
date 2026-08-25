# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        dummy = head
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next

        cri = []
        for i in range(1, len(arr) - 1):
            if (arr[i-1] < arr[i] > arr[i+1]) or (arr[i-1] > arr[i] < arr[i+1]):
                cri.append(i)
        if len(cri) < 2:
            return [-1,-1]

        _min = _max = cri[-1] - cri[0]
        for i in range(len(cri) - 1):
            _min = min(_min, cri[i+1] - cri[i])

        return [_min, _max]
        
