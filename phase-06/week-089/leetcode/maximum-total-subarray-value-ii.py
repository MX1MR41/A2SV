class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [float("inf")] * (2 * self.n)

    def update(self, ind, x):
        ind += self.n

        self.tree[ind] = x
        ind = ind // 2 if not ind % 2 else (ind - 1) // 2

        while ind > 0:
            self.tree[ind] = min(self.tree[2 * ind], self.tree[2 * ind + 1])
            ind = ind // 2 if not ind % 2 else (ind - 1) // 2

    def query(self, l, r):
        l += self.n
        r += self.n

        res = float("inf")

        while l <= r:
            if l % 2:
                res = min(res, self.tree[l])
                l = (l + 1) // 2
            else:
                l //= 2

            if not r % 2:
                res = min(res, self.tree[r])
                r = (r - 2) // 2
            else:
                r = (r - 1) // 2

        return res


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # segment tree + heap + monotonic stack
        # the problem boils down to finding which k subarrays have the biggest values
        # we need to find a way to get those top k without it iterating through all n*(n+1)/2 subarrays
        # to be greedy we can start with the largest numbers and the ranges they cover as the largest in range
        # but since the best ranges could change dynamically as we process ranges, we also need a way to 
        # dynamically keep track of and get the best possible range right now. For this we can use a heap.
        # so initially we find the range for each num within which it is the largest, using monotonic stack
        # to calculate the value for a range, we need to find the minimum number in that range using segment tree
        # then we put the ranges in the heap prioritized by their value into a heap
        # then to process them from the heap one by one, we take the value of the range and add it into our result
        # then we have two options, to narrow the range from either the left or the right, so we calculate those 
        # and put them into the heap
        # we use a set to ensure we process a range once - when we get it from the heap for the first time


        n = len(nums)

        tree = SegmentTree(n)

        for i in range(n):
            tree.update(i, nums[i])

        # to ensure the unique ownership of each range by a single element
        # we can choose to prioritize ownership either from the right side or left side
        # by allowing one range to expand on one side as far as >= and only to > on the other side
        left = [i for i in range(n)]
        stk = []
        for i in range(n):
            num = nums[i]
            while stk and num > stk[-1][1]:
                stk.pop()

            if not stk:
                left[i] = 0
            else:
                left[i] = stk[-1][0] + 1

            stk.append((i, num))

        right = [i for i in range(n)]
        stk = []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            while stk and num >= stk[-1][1]:
                stk.pop()

            if not stk:
                right[i] = n - 1
            else:
                right[i] = stk[-1][0] - 1

            stk.append((i, num))

        heap = []

        used = set()
        for i in range(n):
            maxx = nums[i]
            l = left[i]
            r = right[i]
            if l == r:
                continue

            minn = tree.query(l, r)

            item = (-(maxx - minn), -maxx, i, l, r)
            used.add((l, r))
            heappush(heap, item)

        res = 0
        while heap and k > 0:

            ndiff, nnum, ind, l, r = heappop(heap)

            res += -ndiff
            k -= 1

            if l == r:
                continue

            if ind <= r - 1:
                minn1 = tree.query(l, r - 1)
                opt1 = -nnum - minn1
                item = (-opt1, nnum, ind, l, r - 1)
                if (l, r - 1) not in used:
                    used.add((l, r - 1))
                    heappush(heap, item)

            if ind >= l + 1:

                minn2 = tree.query(l + 1, r)
                opt2 = -nnum - minn2
                item = (-opt2, nnum, ind, l + 1, r)
                if (l + 1, r) not in used:
                    used.add((l + 1, r))

                    heappush(heap, item)

        return res
