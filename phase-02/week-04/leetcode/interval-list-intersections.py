class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans, i, j = [], 0, 0
        n1, n2 = len(firstList), len(secondList)

        while i < n1 and j < n2:

            if firstList[i][1] < secondList[j][0]:
                i += 1

            elif secondList[j][1] < firstList[i][0]:
                j += 1

            elif firstList[i][0] <= secondList[j][0] and secondList[j][1] <= firstList[i][1]:
                ans.append(secondList[j])
                j += 1

            elif secondList[j][0] <= firstList[i][0] and firstList[i][1] <= secondList[j][1]:
                ans.append(firstList[i])
                i += 1

            elif secondList[j][1] > firstList[i][1] >= secondList[j][0]:
                ans.append([secondList[j][0], firstList[i][1]])
                i += 1
                
            elif firstList[i][1] > secondList[j][1] >= firstList[i][0]:
                ans.append([firstList[i][0], secondList[j][1]])
                j += 1

        return ans
