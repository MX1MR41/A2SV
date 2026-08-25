class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # heap
        # simulate the process using two heap pattern
        
        # heap to store the available rooms for use, lowest index first
        available = [i for i in range(n)]
        heapify(available)

        # heap to store occupied rooms in the format of (time_when_room_will_free, room)
        # earliest free rooms first
        occupied = []


        count = Counter()

        # sort the meetings in reverse so we can simply keep popping from the end
        meetings.sort(reverse=True)

        t = 0 # current time

        while meetings:
            # skip ahead to the future when the earliest meeting will start
            t = meetings[-1][0]

            # if no rooms are available, skip ahead to when the earliest a room will be free
            if not available and occupied:
                t = max(t, occupied[0][0])

            # gather all available rooms
            while occupied and occupied[0][0] <= t:
                heappush(available, heappop(occupied)[1])

            # put meetings in rooms, earliest meeting to lowest index room
            while available and meetings and meetings[-1][0] <= t:
                s, e = meetings.pop()

                new_s = t
                new_e = t + (e - s)

                room = heappop(available)

                heappush(occupied, (new_e, room))

                count[room] += 1



        maxx = max(count.values())

        for i in range(n):
            
            if count[i] == maxx:
                return i
