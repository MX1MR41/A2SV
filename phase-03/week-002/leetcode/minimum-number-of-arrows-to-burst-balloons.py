class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort() # sorting is indispensable
        arrowPos = points[0][1] # the best position we can shoot the arrow from to hit most targets
        arrows = 1 # a minimum of 1 arrow is mandatory 

        for i in points[1:]: # traverse from the second element
            if i[0] <= arrowPos: # if the balloon is within the reach of the arrow that was last shot
                arrowPos = min(arrowPos, i[1]) # update the arrow position to the max of the intersection of the balloons
            else: # if the balloon is outside the reach of the the last shot arrow
                arrows += 1 # we neeed another arrow
                arrowPos = i[1]  # and the new arrow will be shot at the end of the current balloon


        return arrows


        