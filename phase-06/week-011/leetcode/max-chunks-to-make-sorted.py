class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # greedy
        # we keep track of the maximum number seen so far
        # and if that max is less than or equal to the current index,
        # that means we have got a previous chunk that could be sorted and be a valid
        # part of the sorted array because it is guaranteed that the biggest element
        # so far is within that previous and upto chunk


        chunks = 0
        _max = -1

        for index, num in enumerate(arr):
            _max = max(_max, num)
            if _max <= index:
                chunks += 1
                _max = -1

        return chunks

        
