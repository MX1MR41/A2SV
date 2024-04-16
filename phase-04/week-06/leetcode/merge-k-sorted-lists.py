# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in lists:
            dummy = i
            while dummy:
                heappush(heap, dummy.val)
                dummy = dummy.next

        n = len(heap)
        # returns a sorted array
        nums = nlargest(n, heap)[::-1]
        
        i = 0
        ans = None
        if nums:
            ans = ListNode(nums[i])
            dummy = ans
            i += 1

            while i < n:
                dummy.next = ListNode(nums[i])
                dummy = dummy.next
                i += 1

        return ans

        
            
        
