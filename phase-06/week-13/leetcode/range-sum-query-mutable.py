class SegmentTree:
    def __init__(self, arr):
        # Initialize the size as the closest power of two greater than or equal to len(arr).
        # Initilaize a tree of zeros with that size.
        # Let's say x = len(arr), and n = the closest power of two gte x;
        # the last n elements of the tree will hold the actual elements of arr,
        # the first element of the tree won't hold anything,
        # the next (n - 1) elements will hold the recursive sum of the last n elements.
        # Essentially, tree is divided into two; first n elements will hold sums(except tree[0])
        # last n elements will hold values of arr.
        # Every left child has an even index and every right child has an odd index.

        self.n = 2 ** (ceil(log2(len(arr)))) 
        self.tree = [0] * (2 * self.n)

        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]

        # Build the tree recursively starting from the second element
        # so the second element or tree[1] will have the total sum of arr
        self.build(1)

    def build(self, i):
        # Base case: if we are in the last n elements, return its value
        if i >= self.n:
            return self.tree[i]

        self.tree[i] = self.build(2 * i) + self.build(2 * i + 1)

        return self.tree[i]

    def update(self, index, value):
        # Fix the offset so it lies in the last n elements then update its value
        index += self.n 
        self.tree[index] = value

        # Update index so it goes to its parent
        if index % 2:
            index = (index - 1) // 2
        else:
            index //= 2

        # Iteratively move upwars parent by parent and update sums accordingly
        while index > 0:
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]
            if index % 2:
                index = (index - 1) // 2
            else:
                index //= 2

    def query(self, left, right):
        # Fix the offset so the indices lie in the last n elements
        left += self.n
        right += self.n

        extra = 0 # Will hold the extra values that aren't paired with their twins

        while left < right:
            # It is unpaired, so include its value and move to right neigboring parent
            if left % 2:
                extra += self.tree[left]
                left = (left + 1) // 2
            else:
                left //= 2

            # It is unpaired, so include its value and move to left neigboring parent
            if not right % 2:
                extra += self.tree[right]
                right = (right - 2) // 2

            else:
                right = (right - 1) // 2

            
        # If left and right merged into one parent, we include its sum
        return self.tree[left] + extra if left == right else extra


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
