class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # check whether the rec2 is either completely to the left, right above or below rec1
        if rec2[2] <= rec1[0] or rec2[0] >= rec1[2] or rec2[1] >= rec1[3] or rec2[3] <= rec1[1]:
            return False
        return True
        
