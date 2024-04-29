class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # use two min heaps, one to store the rooms that are busy along with the time they will be free 
        # and one to store the rooms that are free
        # at each iteration of meeting we check to see if there are any free rooms
        # if so then we just use it. If there are no free rooms, we pick the room from busy rooms
        # that will be free first, and we will update its end time by assigning the meeting in that room
        meetings.sort()
        busy, free = [], [i for i in range(n)]
        heapify(free)

        cnt = defaultdict(int)

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                room = heappop(busy)
                heappush(free, room[1])

            if free:
                room = heappop(free)
                cnt[room] += 1
                heappush(busy, (end, room))
            else:
                first_free, room = heappop(busy)
                cnt[room] += 1

                heappush(busy, (first_free + end - start, room))


        max_meets = max(cnt.values())

        count = 0
        res = []
        for i, j in cnt.items():
            if j == max_meets:
                res.append(i)

        return min(res)

