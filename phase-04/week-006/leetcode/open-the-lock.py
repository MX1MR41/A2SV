class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000": return 0

        dead = set(deadends)

        # returns the next possible patterns a move away from  the given pattern
        def next(current):
            next_patterns = set()
            for i in range(4):
                # since the wheels are circular, we modulo by the number of options i.e. 10
                up = current[:i] + str(((int(current[i]) + 1)) % 10) + current[i+1:]
                next_patterns.add(up)

                down = current[:i] + str(((int(current[i]) - 1)) % 10) + current[i+1:]
                next_patterns.add(down)

            return next_patterns


        def bfs(que, visited):
            path = 0

            while que:
                for _ in range(len(que)):
                    curr = que.popleft()
                    if curr == target: return path

                    if curr in visited: continue
                    visited.add(curr)

                    if curr in dead: continue

                    next_patterns = next(curr)
                    que.extend(next_patterns)

                path += 1

        ans = bfs(deque(["0000"]), set())
        return ans if ans else -1

        

        
