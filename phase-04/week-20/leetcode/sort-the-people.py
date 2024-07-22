class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = list(zip(names, heights))
        zipped.sort(key = lambda x: x[1], reverse = True)
        return [z[0] for z in zipped]
