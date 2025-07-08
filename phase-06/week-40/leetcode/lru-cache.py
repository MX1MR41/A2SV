class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = self.tail = None
        self.map = {}



    def add(self, node):
        """
        Accepts an individual node outside the cache, and adds it to the head

        """
        self.map[node.key] = node
        self.size += 1

        if self.head is None: # First node being added so it is both the head and tail
            self.head = self.tail = node
            return

        # Add it as a head, make its next be the previous head,
        # and make the previous head's prev be this node
        node.next = self.head
        self.head.prev = node
        self.head = node



    def remove(self, node):
        """
        Accepts a node that is somewhere in the cache and removes it

        """
        del self.map[node.key]
        self.size -= 1

        if node == self.head == self.tail: # It is the only node in the cache
            self.head = self.tail = None
            return

        if node == self.head: # The head pointer moves by one forward
            self.head = node.next
            return

        if node == self.tail: # The tail pointer moves by one backward
            self.tail = node.prev
            return

        # Detach it from the middle and re-stitch its neighbours
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]

        # Getting a node means using it, so it needs to come to the head as
        # the most recently used node. For that, we can remove it and add it
        self.remove(node)
        self.add(node)

        return node.val


    def put(self, key: int, value: int) -> None:

        if key in self.map:
            # Same functionality as get() but we update the node's value
            node = self.map[key]
            node.val = value

            self.remove(node)
            self.add(node)

            return


        # Cache is full, so remove the least recently used node i.e. the tail
        if self.size == self.capacity: 
            self.remove(self.tail)

        
        node = Node(key, value)
        self.add(node)
