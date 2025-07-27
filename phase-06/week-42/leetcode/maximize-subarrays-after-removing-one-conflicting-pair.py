class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # heap + sweep line
        # calculate the gain (extra valid subarrays) that could be obtained by removing
        # a conflicint pair for every pair. Then add that to the intial count of valid
        # base subarrays.
        # to compute the gain of removing pair[j] for index i where i is [1...n], 
        # we need to find the closest next conflicting pair, and the gain will be the 
        # distance between the ends of those two pairs. To do that we can maintain the pairs
        # in a heap while iterating backwards from n to 1.
        # to compute the base count of subarrays starting at index i, we iterate backwards
        # from n to 1 and maintain the seen pairs in a heap, that way we can get the 
        # closest conflicting pair's end which is going to be the limit for the subarrays
        # that can be formed with index i as starting point


        for p in conflictingPairs:
            p.sort()

        conflictingPairs.sort()

        gain = defaultdict(int)

        m = len(conflictingPairs)

        heap = []

        j = m - 1

        for i in range(n, 0, -1):
            while j >= 0 and conflictingPairs[j][0] >= i:
                s, e = conflictingPairs[j]
                heappush(heap, (e, j))
                j -= 1

            if heap:
                e, ind = heappop(heap)

                if heap:
                    diff = heap[0][0] - e
                else:
                    diff = n + 1 - e

                gain[ind] += diff

                heappush(heap, (e, ind))

        max_gain = max(gain.values()) if gain.values() else 0

        base = 0

        heap = []
        j = m - 1
        for i in range(n, 0, -1):
            while j >= 0 and conflictingPairs[j][0] >= i:
                s, e = conflictingPairs[j]
                heappush(heap, e)
                j -= 1

            subs = heap[0] - i if heap else n + 1 - i
            base += subs

        return base + max_gain
