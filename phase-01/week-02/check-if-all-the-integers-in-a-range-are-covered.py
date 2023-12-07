class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      set1 = set() # set for the ranges
      set2 = set([j for j in range(left, right + 1)]) # set-ify left to right

      for i in range(len(ranges)):
        set1.update(set([ j for j in range(ranges[i][0], ranges[i][-1] + 1)]))

      return set2.issubset(set1)


        