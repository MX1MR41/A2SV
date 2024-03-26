class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res, temp = [0 for _ in range(len(queries))], []
        # first we take care of the cases where either a and b have already met
        # or one of them is located to the right on a taller building
        # all the other cases, we will store in a custom format for further processing
        for ind, q in enumerate(queries):
            a, b = sorted(q)
            if a == b or heights[a] < heights[b]:
                res[ind] = b
            else:
                temp.append((a, b, ind))

        n = len(heights) - 1
        mono = deque() # a monotonic stack/queuue
        
        for a, b, ind in sorted(temp, key = lambda x: x[1], reverse=True):
            while n > b:
                while mono and heights[mono[0]] < heights[n]:
                    mono.popleft()
                mono.appendleft(n)
                n -= 1
                
            k = bisect_right(mono, heights[a], key=lambda x: heights[x])

            res[ind] = -1 if k == len(mono) else mono[k]

        return res