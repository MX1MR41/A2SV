class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # the number of steps taken has such a pattern 
        # 1, 1, 2, 2, 3, 3, 4, 4, ...
        # and each time, the direction changes in a clockwise manner
        res = []

        d = "r" # initial direction
        nxt = {"r": "d", "d" : "l", "l": "u", "u": "r"} # next direction

        step = 0 # steps taken in the currenyt iteration
        steps = 1 # total number of steps that must be taken in this iteration
        cnt = 0 # count of how many time "steps" have been achieved; if 2, reset

        curr = [rStart, cStart]
        elements = 0
        while elements < rows*cols:


            r, c = curr
            if 0 <= r < rows and 0 <= c < cols:
                res.append([r,c])
                elements += 1

            if d == "r":
                curr[1] += 1
            elif d == "d":
                curr[0] += 1
            elif d == "l":
                curr[1] -= 1
            else:
                curr[0] -= 1

            step += 1
            if step == steps:
                d = nxt[d]
                step = 0
                cnt += 1

                if cnt == 2:
                    cnt = 0
                    steps += 1


        return res

   
