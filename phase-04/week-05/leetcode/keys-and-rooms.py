class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num = len(rooms)
        def bfs(q, visited):
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr in visited: continue
                    visited.add(curr)

                    q.extend(rooms[curr])


        Q, visited = deque([0]), set()

        bfs(Q, visited)


        return len(visited) == num


                
                    
        keys-and-rooms.p
