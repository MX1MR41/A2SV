class SegmentTree:
    def __init__(self, n):
        self.n = int(pow(2, ceil(log2(n))))
        self.tree = [1] * (2 * self.n)

        self.build(1)


    def build(self, ind):
        if ind >= self.n:
            return self.tree[ind]

        self.tree[ind] = self.build(2 * ind) * self.build(2 * ind + 1)

        return self.tree[ind]

    def update(self, ind, value):
        ind += self.n

        self.tree[ind] = value
        parent = ind//2 if not ind % 2 else (ind - 1)//2

        while parent > 0:
        
            self.tree[parent] = self.tree[2 * parent] * self.tree[2 * parent + 1]
            parent = parent//2 if not parent % 2 else (parent - 1)//2

    def query(self, left, right):
        left += self.n
        right += self.n

        prod = 1
        while left < right:
            if left % 2:
                prod *= self.tree[left]
                left = (left + 1)//2
            else:
                left //= 2

            if not right % 2:
                prod *= self.tree[right]
                right = (right - 2)//2
            else:
                right = (right - 1)//2

        prod *= self.tree[left] if left == right else 1

        return prod




class ProductOfNumbers:

    def __init__(self):
        self.tree = SegmentTree(40000)
        self.right = -1

        self.tree.update(self.right, 100)
        result = self.tree.query(0, 3000)

        
        

    def add(self, num: int) -> None:
        # return 
        self.right += 1
        self.tree.update(self.right, num)


    def getProduct(self, k: int) -> int:
        # return 1
        left = max(0, self.right - k + 1)

        result = self.tree.query(left, self.right)
        return result
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
