class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = defaultdict(int)
        for strong, weak in edges:
            indeg[weak] += 1

        res = []
        for i in range(n):
            if not indeg[i]:
                res.append(i)

        return res.pop() if len(res) == 1 else -1
        
