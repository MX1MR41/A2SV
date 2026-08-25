class Solution:
    def racecar(self, target: int) -> int:
        # bfs
        start = (0, 1)

        que = deque([start])
        ops = 0
        seen = set()
        while que:
            for _ in range(len(que)):
                pos, speed = que.popleft()
                if pos == target:
                    return ops
                if (pos, speed) in seen:
                    continue

                seen.add((pos, speed))

                pos1 = pos + speed
                speed1 = 2*speed

                if (pos1, speed1) not in seen:
                    que.append((pos1, speed1))

                pos2 = pos
                speed2 = -1 if speed > 0 else 1
                

                if (pos2, speed2) not in seen:
                    que.append((pos2, speed2))

            ops += 1
        
