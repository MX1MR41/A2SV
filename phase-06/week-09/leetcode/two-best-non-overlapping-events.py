class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # binary search + prefix max + dp
        # Events don't overlap if the start of the latter is greater than the end of the former.
        # For an event, find the max value of a previous nonoverlapping event
        # Store a copy of the events sorted by their end times 
        # Then update the values as prefix max i.e. the maximum value from a previous event.

        # Sort the original by their start times, then binary search over the other array 
        # (the one that is sorted by the end times and contains prefix max values) 
        # to find a the nearest valid nonoverlapping previous event, 
        # which by then would contain the prefix max value, use that

        



        def find(start):
            value = 0
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r)//2
                if byend[mid][1] < start:
                    value = byend[mid][-1]
                    l = mid + 1
                else:
                    r = mid - 1

            return value


        # construct a cop array that is sorted by end times
        byend = [event[::] for event in events]
        byend.sort(key = lambda x: x[1])
        events.sort()

        # if no valid pairs exist, the answer would be the maximum value of an event
        ans = max(event[-1] for event in events)

        # update the array to contain prefix max
        n = len(byend)
        for i in range(1, n):
            byend[i][-1] = max(byend[i][-1], byend[i - 1][-1])

        # for each event, find the closest nonoverlapping event's value
        for i in range(1, n):
            start, end, val = events[i]
            other = find(start)
            ans = max(ans, val + other)


        return ans



