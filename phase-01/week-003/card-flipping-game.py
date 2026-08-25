class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        unique_numbers = set(fronts + backs)
        
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in unique_numbers:
                unique_numbers.remove(fronts[i])
        
        return 0 if not unique_numbers else unique_numbers.pop()
