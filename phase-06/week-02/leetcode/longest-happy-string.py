class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # at each turn choose the most remaining letter, 
        # but if it has a streak of 2, choose another letter to break the streak
        curra, currb, currc = 0, 0, 0
        total = a + b + c
        result = []

        for i in range(total):
            if (a >= b and a >= c and curra != 2) or (a > 0 and (currb == 2 or currc == 2)):

                result.append("a")
                a -= 1
                curra += 1
                currb = currc = 0

            elif (b >= a and b >= c and currb != 2) or (b > 0 and (currc == 2 or curra == 2)):
              
                result.append("b")
                b -= 1
                currb += 1
                curra = currc = 0

            elif (c >= a and c >= b and currc != 2) or (c > 0 and (curra == 2 or currb == 2)):
            
                result.append("c")
                c -= 1
                currc += 1
                curra = currb = 0

        return "".join(result)
