class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # binary search
        # perform binary search over possible y values to find the result


        # calculates the sum areas above and below the cut line
        def divide(cut):
            up = down = 0

            for x, y, l in squares:
                if y <= cut <= y + l:
                    bottom = l*(cut - y)
                    top = l*(y + l - cut)

                    up += top
                    down += bottom
                else:
                    area = l**2

                    if y >= cut:
                        up += area
                    else:
                        down += area

            return up, down
            
        min_y = min(i[1] for i in squares)
        max_y = max(i[1] + i[2] for i in squares)

        res = max_y

        l, r = min_y, max_y

        # while their differnece is greater than than just a degree more
        # than the required precision
        while l + (10**-6) <= r:
            mid = (l + r)/2
            
            up, down = divide(mid)
            
            if down == up:
                res = mid
                r = mid - 10**-6
                
            elif down > up:
                res = mid
                r = mid - 10**-6
            else:
                l = mid + 10**-6

        return res
