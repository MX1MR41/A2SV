# Solution 1
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


# Solution 2
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # queue  + heap
        n = len(nums)

        # 1. Initialize 'q': Sort all queries by their start points.
        #    queries = [[0,2],[0,2],[1,1]] for nums = [2,0,2]
        #    q becomes deque([[0,2], [0,2], [1,1]])
        q = deque(sorted(queries)) # Sorts by first element (l), then second (r) if l's are equal

        # 2. Initialize 'available' and 'working' piles (priority queues)
        available = [] # Min-heap storing -r (to simulate a max-heap of r)
        working = []   # Min-heap storing r (to find earliest ending active query)

        # --- The Sweep Line ---
        # For each index i in our nums array...
        for i in range(n):
            # --- Step A: Add newly relevant queries to the 'available' pile ---
            # Look at queries in 'q' (sorted by start time).
            # If a query [l, r] has its start time l <= current index i,
            # it means this query *could* start working now. Move it from 'q' to 'available'.
            while q and q[0][0] <= i:
                # q[0] is the query [l,r] at the front of the deque
                # q[0][0] is its start point l
                start_l, end_r = q.popleft() # Take it out of q
                # Add its end_r to 'available', negated because 'available' is a min-heap
                # acting as a max-heap for end_r.
                heapq.heappush(available, -end_r)

            # --- Step B: Remove expired queries from the 'working' pile ---
            # Look at queries in 'working' (queries we previously chose).
            # If a chosen query [l, r] has its end point r < current index i,
            # it means this query no longer covers nums[i]. Remove it from 'working'.
            # working[0] is the smallest end_r in the 'working' min-heap.
            while working and working[0] < i:
                heapq.heappop(working) # Remove the query that finished earliest and before i

            # --- Step C: Satisfy nums[i] using 'working' and 'available' ---
            # nums[i] is the target number of decrements for the current element.
            # len(working) is how many decrements nums[i] is already getting
            # from queries we've already committed to.
            while nums[i] > len(working):
                # We need more decrements for nums[i].
                # We need to pick a new query. The best one to pick is from 'available'
                # that covers 'i' and extends furthest to the right.

                # Condition 1: Is there anything in 'available'?
                # Condition 2: Does the best query in 'available' actually cover 'i'?
                #              -available[0] is the largest end_r from the 'available' pile.
                #              If this largest end_r is less than i, then no query in 'available'
                #              can cover i (since all others have even smaller end_r's).
                if available and -available[0] >= i:
                    # Yes, there's a suitable query in 'available'.
                    # Take the best one (largest -r, so smallest -r when popped).
                    best_r_negative = heapq.heappop(available)
                    # Convert it back to a positive end_r and add to 'working'.
                    heapq.heappush(working, -best_r_negative)
                    # Now len(working) has increased by 1, so nums[i] gets one more decrement.
                else:
                    # No suitable query in 'available' to cover nums[i].
                    # This means we cannot satisfy nums[i]. The task is impossible.
                    return -1

        # --- After the Loop ---
        # If we've successfully processed all nums[i] without returning -1,
        # it means we found a set of queries to zero out the array.

        # What does 'len(available)' mean now?
        # 'available' contains queries that:
        #   1. Started (their l was <= some i we processed).
        #   2. Were *never chosen* to be moved to 'working'.
        # These are precisely the queries that we *didn't need to use*.
        # So, these are the queries we can remove.
        # The problem asks for the maximum number of elements that can be removed.
        return len(available)
