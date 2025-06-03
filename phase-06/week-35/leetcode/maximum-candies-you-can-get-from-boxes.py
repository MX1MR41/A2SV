class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # topological sort

        tot = 0
        havebox = set(initialBoxes)
        que = deque([box for box in initialBoxes if status[box] == 1])

        seen = set()
        while que:
            for _ in range(len(que)):
                box = que.popleft()
                if box in seen:
                    continue

                seen.add(box)

                tot += candies[box]

                for openbox in keys[box]:
                    status[openbox] = 1
                    if openbox in havebox:
                        que.append(openbox)

                for inbox in containedBoxes[box]:
                    havebox.add(inbox)

                    if status[inbox] == 1:
                        que.append(inbox)

        return tot

        
