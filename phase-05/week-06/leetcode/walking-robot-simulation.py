class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0

        obstacle_set = set(map(tuple, obstacles))

        x, y = 0, 0
        ans = 0

        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(command):

                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy

                        ans = max(ans, x**2 + y**2)
                    else:
                        break

        return ans
