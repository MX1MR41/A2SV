class Solution:
    def countCollisions(self, directions: str) -> int:
        # two pass

        res = 0

        last = ""
        for d in directions:
            if d == "L":
                if last == "S":
                    res += 1
                elif last == "R":
                    last = "S"
                    res += 1
            else:
                last = d

        last = ""
        for d in directions[::-1]:
            if d == "R":
                if last == "S":
                    res += 1
                elif last == "L":
                    last = "S"
                    res += 1
            else:
                last = d

        return res


        

        
