class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # monotonic stack + binary search
        # For each query, we need to find the nearest index to the right that has a number greater
        # than (or equal to y) for both.
        # This could be managed by maintaining a dynamic increasing monotonic stack starting from
        # the right end of the array.
        # In order to make use of this stack, we need to process our queries in the order in which
        # they are closest to the end of the array.
        # Then for every query, we'll have a monotonic stack that contains all the elements greater
        # than or equal to the y of the query (all valid candidates for y), 
        # over which we can perform a binary search to find a suitable choice for the x of the query


        # "clean the data" i.e. store with indices and reorder x and y
        queries = [(index, min(x, y), max(x, y)) for index, (x, y) in enumerate(queries)]
        # sort them so we have the queries which have their y's closest
        # to the right end of the array to be processed first
        queries.sort(key=lambda x: x[-1], reverse=True)

        stack = []
        current_index = len(heights) - 1 # the index which will be put to the stack currently

        res = dict()

        for ind, x, y in queries:
            # for every element to the right of y that we haven't yet put onto the stack
            # we put them onto the stack in a monotonically increasing way so that 
            # the stop of the stack (end of the array) will have the smallest element
            while current_index >= 0 and current_index >= y:
                h = heights[current_index]

                while stack and stack[-1][-1] < h:
                    stack.pop()

                stack.append((current_index, h))

                current_index -= 1

            # trivial
            if x == y or heights[x] < heights[y]:
                res[ind] = y
                continue
            


            # binary search over the stack to find a suitable and leftmost choice for x.
            # On the stack, the top element is the leftmost element we have seen so far
            left, right = 0, len(stack) - 1

            ans = left
            while left <= right:
                mid = (left + right) // 2
                if stack[mid][1] > heights[x]:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if stack[ans][1] > heights[x] and stack[ans][1] > heights[y]:
                res[ind] = stack[ans][0]
            else:
                res[ind] = -1

        return [i[1] for i in sorted(res.items())]
