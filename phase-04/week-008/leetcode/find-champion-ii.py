class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        lose = set()
        for strong, weak in edges:
            lose.add(weak)

        res = []
        for i in range(n):
            if i not in lose:
                if res: return -1
                res.append(i)

        return res.pop()

        
