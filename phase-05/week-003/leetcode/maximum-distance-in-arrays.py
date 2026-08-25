class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # greedy approach using heap
        # we just have to choose one max and one min which are from two different arrays
        # we store each max and min with their array index in their respective heaps
        # and we compute the answer using a min and a max with different indices
        maxheap = []
        minheap = []
        for ind, arr in enumerate(arrays):
            heappush(maxheap, (-arr[-1], ind))
            heappush(minheap, (arr[0], ind))


        dist = 0

        _max, _min = heappop(maxheap), heappop(minheap)
        if _min[1] == _max[1]:
            if maxheap and minheap:
                _max2, _min2 = heappop(maxheap), heappop(minheap)
                dist = max(dist, abs(-_max[0] - _min2[0]))
                dist = max(dist, abs(-_max2[0] - _min[0]))
                if _max2[1] != _min2[1]:
                    dist = max(dist, abs(-_max2[0] - _min2[0]))
        else:
            dist = max(dist, abs(-_max[0] - _min[0]))


        return dist

