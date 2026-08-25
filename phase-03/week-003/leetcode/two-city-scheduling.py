class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        margin = [] # arr to hold the margin (profit) of sending to city A rather than B for each
        A = B = 0

        for a, b in costs:
            margin.append([b - a, a, b]) # store the margin along with the original values

        margin.sort()

        for i in range(len(margin)):

            if i < len(margin) / 2:
                A += margin[i][2] # send to A until we reach half of all
            else:
                B += margin[i][1]

        

        return A + B