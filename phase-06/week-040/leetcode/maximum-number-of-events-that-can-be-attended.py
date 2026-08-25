class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # heap + sorting + greedy
        # for a day d, if there are multiple events that span it, it would be better
        # to choose the event which will end the soonest
        # so while traversing through time day by day, we keep track of the events that
        # are happening currently on this day in a heap sorted by their end so that the
        # event whose end is the soonest is a the top of the heap. We also need to get
        # rid of events that were already in our heap but whose end time was past today.
        # finally, we choose to attend the event which is at the top of the heap, i.e.
        # the one which will end the soonest
        
        events.sort(reverse = True)

        heap = []

        total = 0

        start = events[-1][0]
        end = max([event[1] for event in events])

        for day in range(start, end + 1):
            while events and events[-1][0] <= day:
                s, e = events.pop()
                heappush(heap, (e, s))

            while heap and heap[0][0] < day:
                heappop(heap)

            if heap:
                heappop(heap)
                total += 1

        return total


        
