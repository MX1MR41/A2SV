class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        chairs = sorted([arrival, leave, person] for person, (arrival, leave) in enumerate(times))

        heap = []

        free_chairs = []

        chair_assignment = {}

        next_free_chair = 0

        for arrival, leave, person in chairs:

            while heap and heap[0][0] <= arrival:
                _, freed_chair = heappop(heap)
                heappush(free_chairs, freed_chair)

            if free_chairs:
                assigned_chair = heappop(free_chairs)
            else:
                assigned_chair = next_free_chair
                next_free_chair += 1

            chair_assignment[person] = assigned_chair

            heappush(heap, (leave, assigned_chair))

            if person == targetFriend:
                return assigned_chair
