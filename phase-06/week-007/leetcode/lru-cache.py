# Definition of node for a doubly-linked listed
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# store key value pairs in a doubly-linked list with most recently used vals at the head
# use a hashmap to map every key to point to respective node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = defaultdict(lambda : -1) # if element doesnt't exits, return -1
        self.head = None
        self.tail = None

        

    def get(self, key: int) -> int:
        # when getting an element, bring it to the head of the linked list because
        # it has become the most recently used one

        node = self.map[key]

        # if the node doesnt't exist, return -1
        if node == -1:
            return -1

        # if it is the head, return its value without doing any changes
        if self.head == node:
            return node.value

        # if it is the tail (and not the head), cut it off and bring it to the head
        if self.tail == node:
            # adjust tail
            self.tail.prev.next = None
            self.tail = self.tail.prev

            # adjust node
            node.prev = None
            node.next = self.head

            # adjust head
            self.head.prev = node
            self.head = node

            return node.value

        # if the node is neither the tail or head, cut it off and re-stitch its neighbors
        # then attach the node as the head
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev

        node.next = self.head
        self.head.prev = node
        self.head = node

        return node.value

    def put(self, key: int, value: int) -> None:
        # putting a new value also appends the new node to the head since it is the 
        # most recently used one

        node = self.map[key]
        # if the node already exists, bring it the the head (which the get does)
        # and adjust its value
        if node != -1:
            self.get(key)
            self.head.value = value
            return

        node = Node(key, value)
        # if the capacity has been reached, evict the least recently used node
        # i.e. the tail
        if self.size == self.capacity:
            # if the capacity if 1, we only need to delete previous singular key 
            # then assign the new node as both head and tail
            if self.size == 1:
                evict = self.head.key
                del self.map[evict]
                self.head = self.tail = node
                self.map[key] = node
                return 

            # adjust node
            node.next = self.head

            # adjust head
            self.head.prev = node
            self.head = self.map[key] = node
            
            # adjust tail and delete previously tail node
            del self.map[self.tail.key]
            self.tail = self.tail.prev
            self.tail.next = None
            

        else:
            # first node
            if self.size == 0:
                self.head = self.tail = node
                self.size += 1
                self.map[key] = node
                return 

            # add node as the head, map it and increase size by 1
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.map[key] = node
            self.size += 1





        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
