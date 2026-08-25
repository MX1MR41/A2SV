class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.last = -1

    def getNode(self, i):
        if i < 0 or i > self.last:
            return None
        
        dummy = self.head
        while dummy and i > 0:
            dummy = dummy.next
            i -= 1
        return dummy

    def get(self, index: int) -> int:
        node = self.getNode(index)
        if node:
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        add = Node(val)
        if self.head:
            add.next = self.head
        self.head = add
        self.last += 1

    def addAtTail(self, val: int) -> None:

        add = Node(val)

        if not self.head:
            self.head = add
        else:
            dummy = self.head
            while dummy.next:
                dummy = dummy.next
            dummy.next = add

        self.last += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.addAtHead(val)
            return

        prev_node = self.getNode(index - 1)

        if not prev_node:
            return

        add = Node(val)
        add.next = prev_node.next
        prev_node.next = add
        
        self.last += 1

    def deleteAtIndex(self, index: int) -> None:

        if index == 0:
            if self.head:
                self.head = self.head.next
                self.last -= 1
            return

        prev_node = self.getNode(index - 1)

        if not prev_node or not prev_node.next:
            return

        prev_node.next = prev_node.next.next
        self.last -= 1
