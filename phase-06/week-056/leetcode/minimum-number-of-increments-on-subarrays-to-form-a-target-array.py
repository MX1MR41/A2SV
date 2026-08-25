class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update_range(self, l, r, val):
        l += self.n
        r += self.n

        while l < r:
            if l % 2:
                self.tree[l] += val
                l = (l + 1)//2
            else:
                l //= 2

            if not r % 2:
                self.tree[r] += val
                r = (r - 2)//2
            else:
                r = (r - 1)//2

        if l == r:
            self.tree[l] += val

    def query_point(self, x):
        x += self.n
        total = 0

        while x > 0:
            total += self.tree[x]

            if x % 2:
                x = (x - 1)//2
            else:
                x //= 2

        return total


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # monotonic stack + heap + segment tree
        # when we apply an operation on index i and nums[i], we can safely apply it upto the left
        # as far as i - l where nums[i] is less than or equal to all numbers from i to i - l,
        # and to the right as far as i + r where nums[i] is less than or equal to all numbers
        # from i to i + r. So we initially need to find the range within which each number is the
        # minimum; for this we can use monotonic stack.
        # As for order of operations, we need to operate on indices that have the widest 
        # effects first then continue to indices with narrower effects; for this we can use a heap
        # When we want to perform an operation on an index, we need to know how many if any 
        # operations have yet been performed on this index, and we need to apply the operation over
        # the range within which nums[index] is the minimum, i.e. we need to perform point querires
        # and range updates. For this we can use an inverse segment tree

        n = len(target)

        left_bound = [i for i in range(n)]

        stk = []
        for i in range(n):
            num = target[i]
            left = i
            while stk and stk[-1][0] >= num:
                _, new_left = stk.pop()
                left = new_left

            left_bound[i] = left
            stk.append((num, left))


        right_bound = [i for i in range(n)]
        stk = []
        for i in range(n - 1, -1, -1):
            num = target[i]
            right = i
            while stk and stk[-1][0] >= num:
                _, new_right = stk.pop()
                right = new_right

            right_bound[i] = right
            stk.append((num, right))


        heap = []
        for i in range(n):
            num = target[i]
            left, right = left_bound[i], right_bound[i]
            length = right - left + 1
            heappush(heap, (-length, num, i))

        tree = SegmentTree(n)
        ops = 0
        while heap:
            length, num, ind = heappop(heap)
            left, right = left_bound[ind], right_bound[ind]

            deduct = tree.query_point(ind)

            num -= deduct
            if num <= 0:
                continue

            ops += num

            tree.update_range(left, right, num)

        return ops





        
