class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])

        for i in ghosts:
            dist_i = abs((i[0] - target[0])) + abs((i[1] - target[1]))
            if dist_i <= dist:
                return False



        return True
        