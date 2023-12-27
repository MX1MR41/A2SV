class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []

        d = {i:x for i,x in zip(heights,names)}

        n =  len(heights)

        for i in range(1, n):
            m = heights[i]
            j = i -1
            while j >= 0 and m < heights[j]:
                heights[j+1] = heights[j]
                j -= 1

            heights[j+1] = m

        for i in heights[::-1]:
            ans.append(d[i])

        return ans

           
        