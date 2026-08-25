class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = list(s.split())
        longest = max(arr, key= lambda x:len(x))
        result = ["" for i in range(len(longest))]
        matrix = [["" for i in range(len(arr))] for j in range(len(longest))]

        for i in range(len(arr)):
            for j in range(len(arr[i])):
              
                matrix[j][i] += arr[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                if not matrix[i][j]:
                    result[i] += ' '
                else:
                    result[i] += matrix[i][j]
        


        return [res.rstrip() for res in result]