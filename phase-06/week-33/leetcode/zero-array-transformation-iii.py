class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (2 * self.n)

    def update_range(self, l, r, val):
        """
        To modify a range in a segment tree, we apply the updates on select nodes rather than 
        every node up the tree. 
        Updating the value of a node means that its changes will also propagate to its children,
        so we update a parent node's value if and only if that change happens throughout 
        all of its children. For example, adding +1 to node i means all nodes from 2*i to 2*i + 1
        will have +1 added to them. So for an inclusive perfect range like that, we update the 
        parent and not the children. But if the children happend to be outside of the perfect
        inclusive range, we need to update their value because the updated range's parent's range
        doesn't include those children.
        
        The logic is simliar to how query works in normal segment tree but this time we are 
        performing changes on nodes instead of accumulating the values in nodes
        """
        l += self.n
        r += self.n

        while l < r:

            if l % 2:
                self.tree[l] += val
                l = (l + 1) // 2
            else:
                l //= 2

            if not r % 2:
                self.tree[r] += val
                r = (r - 2) // 2
            else:
                r = (r - 1) // 2

        self.tree[l] += val if l == r else 0

    def query_index(self, ind):
        """
        The process is similar to how we query a range in a normal segment tree but this time
        we accumulate the values of a node and its ancestors
        """
        ind += self.n

        res = 0

        while ind > 0:
            res += self.tree[ind]
            ind = ind // 2 if not ind % 2 else (ind - 1) // 2

        return res


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # segment tree + heap
        # Sort queries.
        # For every index i, gather all the queries that can affect i and put them in a heap
        # so that the query with the farthest end will be at the top of the heap.
        # To get the total deductions that happened on i from previous processing intervals,
        # use a modified segment tree that performs update on range and perfoms query on index.
        # After performing the deductions, if nums[i] is still > 0, keep taking queries from the
        # heap and applying them. Everytime a query is applied, the segment tree will update the
        # range and and the count of queries we used will increase by 1. 
        # Since the heap will always give the farthest ending query, the greedy choice of 
        # minimum number of queries is guaranteed.

        n = len(nums)
        tree = SegmentTree(n)

        queries.sort()

        used = 0

        heap = []
        j = 0

        for i in range(n):

            while j < len(queries) and queries[j][0] <= i <= queries[j][1]:
                heappush(heap, (-queries[j][1], queries[j][0]))
                j += 1

            delta = tree.query_index(i)

            nums[i] -= delta

            while nums[i] > 0 and heap:
                end, start = heappop(heap)
                end = -end

                tree.update_range(start, end, 1)

                used += 1
                nums[i] -= 1 if start <= i <= end else 0

            if nums[i] > 0:
                return -1

        return len(queries) - used
