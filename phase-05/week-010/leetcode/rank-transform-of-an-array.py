class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_set = sorted(list(set(arr)))
        rank = dict()
        for ind, num in enumerate(sorted_set):
            rank[num] = ind + 1

        ans = [rank[num] for num in arr]
        return ans
        
