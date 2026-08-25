class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [z[0] for z in sorted(list(zip(names, heights)), key = lambda x: x[1], reverse = True )]
