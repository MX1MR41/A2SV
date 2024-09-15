import sys
from collections import defaultdict, deque

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

q = int(input())
queries = [input().split() for i in range(q)]

head = ListNode(None) 
tail = ListNode(None, prev=head) 
head.next = tail

positions = defaultdict(lambda :deque())

for query in queries:
    operation = query[0]
    if operation == 'insert':
        x, y = map(int, query[1:])
        new_x = ListNode(x)
        if positions[y]:
            first_y = positions[y][0]
            temp = first_y.next
            new_x.prev = first_y
            new_x.next = temp
            first_y.next = new_x
            temp.prev = new_x
            positions[x].append(new_x)
        else:
            temp = tail.prev
            temp.next = new_x
            tail.prev = new_x
            new_x.next = tail
            new_x.prev = temp
            positions[x].append(new_x)
    
    else:
        w = int(query[1])
        if positions[w]:
            target = positions[w].popleft()
            prev = target.prev
            nxt = target.next
            prev.next = nxt
            nxt.prev = prev

ans = []
current = head.next
while current.val != None:
    ans.append(current.val)
    current = current.next

print(*ans)