class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # similar to https://leetcode.com/problems/merge-intervals/

        x = [[rect[0], rect[2]] for rect in rectangles]
        y = [[rect[1], rect[3]] for rect in rectangles]

        x.sort()
        y.sort()

        xcuts = 0
        for i in range(1, len(x)):
            s, e = x[i]
            
            if s >= x[i-1][-1]:
                # separate, so can be cut
                xcuts += 1
            else:
                # update the maximum end 
                x[i][1] = max(e, x[i -1][-1])
        
        if xcuts >= 2:
            return True

        ycuts = 0
        for i in range(1, len(y)):
            s, e = y[i]
            if s >= y[i-1][-1]:
                ycuts += 1
                
            else:
                y[i][1] = max(e, y[i -1][-1])
        
        if ycuts >= 2:
            return True


        return False




        
