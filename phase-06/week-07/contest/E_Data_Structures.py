class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.lazy_start_a = -1  # Start index in array `a` for lazy propagation
        self.lazy_start_b = -1  # Start index in array `b` for lazy propagation


class SegmentTree:
    def __init__(self, n):
        self.tree = [None] * (4 * n)  # Tree array to store nodes
        self.n = n
        self.build(1, n, 1)

    def build(self, left, right, node_index):
        """Builds the segment tree."""
        self.tree[node_index] = SegmentTreeNode(left, right)
        if left == right:  # Leaf node
            return
        mid = (left + right) // 2
        self.build(left, mid, node_index * 2)
        self.build(mid + 1, right, node_index * 2 + 1)

    def update_range(self, left, right, start_a, start_b, node_index=1):
        """Updates the range [left, right] lazily with start indices."""
        node = self.tree[node_index]
        if node.start == left and node.end == right:
            node.lazy_start_a = start_a
            node.lazy_start_b = start_b
            return
        self.propagate(node_index)  # Propagate lazy values to children
        mid = (node.start + node.end) // 2
        if right <= mid:
            self.update_range(left, right, start_a, start_b, node_index * 2)
        elif left > mid:
            self.update_range(left, right, start_a, start_b, node_index * 2 + 1)
        else:
            self.update_range(left, mid, start_a, start_b, node_index * 2)
            self.update_range(mid + 1, right, start_a, start_b, node_index * 2 + 1)

    def propagate(self, node_index):
        """Propagates lazy updates to children."""
        node = self.tree[node_index]
        if node.lazy_start_a != -1:
            left_child = self.tree[node_index * 2]
            right_child = self.tree[node_index * 2 + 1]
            left_child.lazy_start_a = node.lazy_start_a
            left_child.lazy_start_b = node.lazy_start_b
            right_child.lazy_start_a = node.lazy_start_a
            right_child.lazy_start_b = node.lazy_start_b
            node.lazy_start_a = -1
            node.lazy_start_b = -1

    def query(self, index, node_index=1):
        """Finds the value at position `index` in the segment tree."""
        node = self.tree[node_index]
        if node.start == node.end:
            return node.lazy_start_a, node.lazy_start_b
        self.propagate(node_index)
        mid = (node.start + node.end) // 2
        if index <= mid:
            return self.query(index, node_index * 2)
        else:
            return self.query(index, node_index * 2 + 1)



n, m = map(int, input().split())
array_a = [0] + list(map(int, input().split()))  
array_b = [0] + list(map(int, input().split()))  
segment_tree = SegmentTree(n)


for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:  
        start_a, start_b, length = query[1:]
        segment_tree.update_range(start_b, start_b + length - 1, start_a, start_b)
    elif query[0] == 2:  
        position = query[1]
        start_a, start_b = segment_tree.query(position)
        if start_a == -1:  
            print(array_b[position])
        else:
            print(array_a[position - start_b + start_a])

