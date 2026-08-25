class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        def merge(left, right):
            res = []
            lp = rp = 0

            while lp < len(left) and rp < len(right):
                if left[lp] <= right[rp]:
                    res.append(left[lp])
                    lp += 1
                else:
                    res.append(right[rp])
                    rp += 1

            res.extend(right[rp:])
            res.extend(left[lp:])
            return res

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
        
            return merge(left_half, right_half)

        nodes = []
        dummy = head
    

        while dummy:
            v = dummy.val
            nodes.append(v)
            dummy = dummy.next


        nodes = mergeSort(0, len(nodes)-1, nodes)


        dummy = head = ListNode(nodes[0])

        for i in nodes[1:]:
            dummy.next = ListNode(i)
            dummy = dummy.next

        return head

        
        