"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def getlast(node, par):
            dummy = node
            prev = par
            
            while dummy:
                if dummy.child:
                
                    last = getlast(dummy.child, dummy)
                
                    last.next = dummy.next
                    if dummy.next:
                        dummy.next.prev = last

                    child = dummy.child
                    child.prev = dummy
                    dummy.next = child

                    dummy.child = None
                    prev = last
                   
                    dummy = last.next
                else:

                    prev = dummy
                    
                    dummy = dummy.next

                
            return prev

        getlast(head, None)
        

        return head



        


        
