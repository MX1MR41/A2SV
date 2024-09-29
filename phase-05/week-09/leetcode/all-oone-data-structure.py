class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_nodes = {}
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, new_node, prev_node, next_node):
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.count_nodes[node.count]

    def inc(self, key: str) -> None:
        current_count = self.key_count.get(key, 0)
        new_count = current_count + 1
        self.key_count[key] = new_count

        if new_count not in self.count_nodes:
            new_node = Node(new_count)
            self.count_nodes[new_count] = new_node
            if current_count == 0:
                self._add_node(new_node, self.head, self.head.next)
            else:
                self._add_node(new_node, self.count_nodes[current_count], self.count_nodes[current_count].next)

        self.count_nodes[new_count].keys.add(key)
        
        if current_count > 0:
            self.count_nodes[current_count].keys.remove(key)
            if not self.count_nodes[current_count].keys:
                self._remove_node(self.count_nodes[current_count])

    def dec(self, key: str) -> None:
        current_count = self.key_count[key]
        new_count = current_count - 1

        if new_count > 0:
            self.key_count[key] = new_count
            if new_count not in self.count_nodes:
                new_node = Node(new_count)
                self.count_nodes[new_count] = new_node
                self._add_node(new_node, self.count_nodes[current_count].prev, self.count_nodes[current_count])

            self.count_nodes[new_count].keys.add(key)
        else:
            del self.key_count[key]

        self.count_nodes[current_count].keys.remove(key)
        if not self.count_nodes[current_count].keys:
            self._remove_node(self.count_nodes[current_count])

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
